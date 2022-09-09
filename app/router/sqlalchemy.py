from fastapi import Response, status,HTTPException, Depends,APIRouter
from sqlalchemy .orm import Session
from app import models,schema,utils,oauth2
from ..database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter()

@router.get("/sqlalchemy")
def testpost(db : Session = Depends(get_db)):
    p=db.query(models.Fastapisample).all()
    return {"msg":p}

@router.post("/sqlcreate",status_code=status.HTTP_201_CREATED,response_model=schema.Postmethod)
def createdb(Post:schema.sqlmethod ,db : Session = Depends(get_db)): 
    # new = models.Fastapisample(title=Post.title,content=Post.content,published=Post.published)
    new = models.Fastapisample(**Post.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new

@router.get("/sqlget/{id}")
def getposts(id: int,db : Session = Depends(get_db)):
    p=db.query(models.Fastapisample).filter(models.Fastapisample.id== id).all()
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} was not found")
    return {"postdetail":p}

@router.delete("/sqldel/{id}",status_code=status.HTTP_204_NO_CONTENT)
def deletepost(id:int,db : Session = Depends(get_db)):
    p=db.query(models.Fastapisample).filter(models.Fastapisample.id== id)
    if p.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    p.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/sqlupdate/{id}")
def updatepost(id: int, Post:schema.sqlmethod,db : Session = Depends(get_db)):
    p=db.query(models.Fastapisample).filter(models.Fastapisample.id== id)
    data = p.first()

    if data == None:        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    p.update(Post.dict(),synchronize_session=False)
    db.commit()
    return {"Msg":p.first()} 

@router.post("/login",response_model=schema.Token)
def login(data: OAuth2PasswordRequestForm = Depends(),db : Session = Depends(get_db)):
    print("email")
    mail=db.query(models.Login).filter(models.Login.email== data.username).first() 
    if not mail:
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    if not utils.verify(data.password,mail.pwd):
        return HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    
    access_token = oauth2.create_access_token(data={"user_id":mail.id})
    return {"access_token":access_token,"token_type":"bearer","id":mail.id}


@router.post("/reg",status_code=status.HTTP_201_CREATED,response_model=schema.register)
def createdb(Post:schema.reg,db : Session = Depends(get_db)): 
    msg=db.query(models.Login).filter(models.Login.email== Post.email).first()
    if  msg:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Email id already registered")
    else:
        hashed_pwd= utils. hash(Post.pwd)
        Post.pwd = hashed_pwd
        new = models.Login(**Post.dict())
        db.add(new)
        db.commit()
        db.refresh(new)
    return {"id":new.id , "email":new.email}

@router.post("/Post",status_code=status.HTTP_201_CREATED,response_model = schema.Post)
def create_post(Post:schema.sqlmethod ,db : Session = Depends(get_db),get_user: int= Depends(oauth2.get_current_user)): 
    print(get_user)
    new = models.Fastapisample(owner_id = get_user.id,**Post.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new
  

@router.get("/sqlgetauth",response_model=schema.Post)
def getposts(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    print(get_user)
    p=db.query(models.Fastapisample).first()
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{get_user.id} was not found")
    return p

@router.delete("/sqldelauth",status_code=status.HTTP_204_NO_CONTENT)
def deletepost(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    p=db.query(models.Fastapisample).filter(models.Fastapisample.owner_id== get_user.id)
    if p.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {get_user.id} does not exist")
    q=p.first()
    if q.owner_id != get_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="No authorised to perform requested action")

    p.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/sqlupdateauth/{id}")
def updatepost(id:int,Post:schema.sqlmethod,db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    p=db.query(models.Fastapisample).filter(models.Fastapisample.id== id)
    data = p.first()

    if data == None:        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    # q=p.first()
    if data.owner_id != get_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="No authorised to perform requested action")

    p.update(Post.dict(),synchronize_session=False)
    db.commit()
    return {"Msg":p.first()} 

@router.get("/sqlselectauth",response_model=schema.sqlmethod)
def testpost(db : Session = Depends(get_db),get_user : int= Depends(oauth2.get_current_user)):
    p=db.query(models.Fastapisample).filter(models.Fastapisample.owner_id==get_user.id).all()
    if not p:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not Found")

    return {"msg":p}