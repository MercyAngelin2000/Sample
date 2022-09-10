from fastapi import APIRouter
import time
import psycopg2  
from psycopg2.extras import RealDictCursor  #to get the column attributes or column names 

router = APIRouter()

@router.get("/")
def getmethod():
    return {"msg": "Hai Mylu Iam Juju"}
    

# while True:                #until the database connection is true, it will not go to another functions
#     try:
#         con = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="postgres", cursor_factory=RealDictCursor)
#         cur = con.cursor()
#         print("Databse connection successfully created")
#         break    #once the db connected the loop will be exit
#     except Exception as error:
#         print("Connection Failed")
#         print("error",error)
#         time.sleep(3)    #it will display error at every 3 mins once until the db connection fails

# myposts = [{"title": "Mercy1","content":"This is Mercy","id":1},{"title": "Mercy2","content":"My nick name is Juju","id":2 },{"title": "Mercy3","content":"Iam also known as Mylu","id":3}] #Global variable declaration
# #[] to get collection post, global variable declaration

# @router.get("/fetch")
# def root():
#     cur.execute("""SELECT * FROM fastapisample """)
#     posts = cur.fetchall()                         #fetching all the data in database
#     print(posts)
#     return {"Msg":posts}

# @router.post("/create",status_code=status.HTTP_201_CREATED)
# def createdb(Post:schema.dbmethod): #assigning class to Post variable
#     cur.execute(""" INSERT INTO fastapisample (id,title, content, published) VALUES (%s,%s,%s,%s) RETURNING * """,
#                 (Post.id,Post.title, Post.content, Post.published))    #used for inserting one row
#     new = cur.fetchone()
#     con.commit()
#     return {"Data":new}

# @router.get("/getmethod/{id}")
# def getposts(id: int):
#     cur.execute(""" SELECT * FROM fastapidemo WHERE id= %s """,(str(id)))
#     getsinglerow = cur.fetchone()
#     if not getsinglerow:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} was not found")
#     return {"postdetail":getsinglerow}

# @router.delete("/delmethod/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def deletepost(id:int):
#     cur.execute("""DELETE FROM fastapidemo WHERE id = %s RETURNING * """,(str(id)))
#     delpost = cur.fetchone()
#     con.commit()
#     if delpost == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
#     return {"message":delpost}

# @router.put("/updatemethod/{id}")
# def updatepost(id: int, Post:schema.dbmethod):
#     cur.execute(f"""UPDATE fastapidemo SET id = %s, title = %s, content = %s, published = %s WHERE id = {str(id)} RETURNING *""",
#                 (Post.id,Post.title,Post.content,Post.published))
                
#     uppost = cur. fetchone()
#     con.commit()
#     if uppost == None:        
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
#     return {"data":uppost}        



# @router.post("/postmethod")
# def postmethod(Post: schema.post): #Post variable, post class name
#     print(Post.dict()) #To display all the values in dict
#     # print(Post.Hai) #to display hai property value
#     # print(Post.Iam) #to display Iam property value
#     # print(Post.DoULoveMe)
#     # print(Post.IsItTrue)
#     # print(Post.TellMeUrAge)
#     return {"msg":Post} #Post is a variable which will return all value to display

# @router.post("/post")
# def postmethod(ms: dict = Body(...)):
#     print(ms)
#     return {"msg": f"Hai{ms['Hai']} Iam{ms['Iam']}"}

# @router.post("/postmethod1",status_code=status.HTTP_201_CREATED)
# def createpost(Post: schema.post): #assigning class to Post variable
#     postDict=Post.dict() #Post la irukka values postdict ku store pannura
#     postDict['id'] = randrange(0,1000000000) #to use id randomly
#     myposts.append(postDict) #appending mypost values to postDict
#     return {"Data":myposts}

# def findpost(id):
#     for p in myposts:                       #it has been created to display the specific id value
#         if p["id"] == id:
#             return p


# # @app.get("/postmethod1/{id}")
# # def getposts(id: int, response:Response):
# #     post = findpost(id) #here post is a variable not class     #Another method to display the status code
# #     if not post:
# #         response.status_code= status.HTTP_404_NOT_FOUND
# #         return {"msg":f"post with id:{id} was not found"}    
# #     return {"postdetail":post}

# @router.get("/postmethod1/{id}")
# def getposts(id: int):
#     post = findpost(id) #here post is a variable not class
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} was not found")
#     return {"postdetail":post}

# @router.get("/post/latest")
# def getlatestpost():
#     post=myposts[len(myposts)-1]                  #to get latest post value
#     return {"detail":post}

# def findindex(id):
#     for i,p in enumerate(myposts):
#         if p['id'] == id:               #here i is index and p is iterate variable
#             return i



# @router.delete("/postmethod1/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def deletepost(id:int):
#     # deleting the post, find the index in array that has required id, use pop method
#     index = findindex(id)

#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     myposts.pop(index)
#     return {"message":" post was successfully deleted"}

# @router.put("/putmethod/{id}")
# def updatepost(id: int, post:schema.post):  #Assigning Schema to post variable
#     index = findindex(id)         #finding the specified index

#     if index == None:        
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
#     postdict = post.dict()      #sending schema value as dict to postdict
#     postdict['id']=id         #checks whether id matches with sent id
#     myposts[index] = postdict     #assinging the updated value to myposts
#     return {"data":postdict}        #returning data
