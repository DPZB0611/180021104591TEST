Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle                
turtle.setup(650,350,200,200)
turtle.penup()          
turtle.fd(-250)               
turtle.pendown()              
turtle.pensize(25)            
turtle.pencolor("purple")     
turtle.seth(-40)        
for i in range(4):      
    turtle.circle(40,80)     
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()
