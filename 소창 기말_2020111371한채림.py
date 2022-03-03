from tkinter import *
import random 


rspList=["가위.gif","바위.gif","보.gif"]  #사진 이름 담은 리스트
rspBig=["가위_big.gif","바위_big.gif","보_big.gif"]#사진 이름 담은 리스트
result=["이겼습니다.","졌습니다.","비겼습니다."] #결과 3가지 담은 리스트(여러번 적기 번거로워서)

##전역 변수 선언##
Ucount=0 #유저의 이긴횟수 측정 변수
Ccount=0 #컴퓨터의 이긴 횟수 측정 변수


##함수 선언##
#가위=0,바위=1,보=2
def clickRock(): #유저가 바위 버튼을 클릭했을 때의 함수
    global Ucount #전역변수 사용을 위해
    global Ccount
    userN=1
    #유저 사진 출력
    userPhoto=PhotoImage(file="C:/Users/allab/Desktop/RSP/"+rspBig[userN])#사진위치입력
    uLabel.configure(image=userPhoto)
    uLabel.image=userPhoto
    #컴퓨터 사진 출력
    comN=random.randrange(3)
    comPhoto=PhotoImage(file="C:/Users/allab/Desktop/RSP/"+rspBig[comN])
    cLabel.configure(image=comPhoto)
    cLabel.image=comPhoto
    #컴퓨터:n승 ,유저:n승 이겼습니다 출력
    if (userN+1)%3 == comN: #유저 짐
        #이깃 횟수 측정 변수를 결과에 맞게 증가 시킴
        Ucount+=0
        Ccount+=1
        comResult.configure(text="computer:"+str(Ccount)+"승")
        userResult.configure(text="user:"+str(Ucount)+"승")
        ResultText.configure(text=result[1])
    elif userN == comN:#컴퓨터와 유저가 비겼을 때
        Ucount+=0
        Ccount+=0
        comResult.configure(text="computer:"+str(Ccount)+"승")
        userResult.configure(text="user:"+str(Ucount)+"승")
        ResultText.configure(text=result[2])
    else:#유저가 이겼을 때
        #이깃 횟수 측정 변수를 결과에 맞게 증가 시킴
        Ucount+=1
        Ccount+=0
        comResult.configure(text="computer:"+str(Ccount)+"승")
        userResult.configure(text="user:"+str(Ucount)+"승")
        ResultText.configure(text=result[0])
        
def clickScissor():#유저가 가위버튼을 클릭했을 때의 함수
    #사진 출력
    global Ucount
    global Ccount
    userN=0
    #유저 사진 출력
    userPhoto=PhotoImage(file="C:/Users/allab/Desktop/RSP/"+rspBig[userN])
    uLabel.configure(image=userPhoto)
    uLabel.image=userPhoto
    #컴퓨터 사진 출력
    comN=random.randrange(3)
    comPhoto=PhotoImage(file="C:/Users/allab/Desktop/RSP/"+rspBig[comN])
    cLabel.configure(image=comPhoto)
    cLabel.image=comPhoto
    #컴퓨터:n승 ,유저:n승 이겼습니다 출력
    if (userN+1)%3 == comN: #유저 패
        Ucount+=0
        Ccount+=1
        comResult.configure(text="computer:"+str(Ccount)+"승")
        userResult.configure(text="user:"+str(Ucount)+"승")
        ResultText.configure(text=result[1])
    elif userN == comN: #유저와 컴퓨터 비김
        Ucount+=0
        Ccount+=0
        comResult.configure(text="computer:"+str(Ccount)+"승")
        userResult.configure(text="user:"+str(Ucount)+"승")
        ResultText.configure(text=result[2])  
    else:#유저 승
        Ucount+=1
        Ccount+=0
        comResult.configure(text="computer:"+str(Ccount)+"승")
        userResult.configure(text="user:"+str(Ucount)+"승")
        ResultText.configure(text=result[0])
        
def clickPaper():
    userN=2
    #사진 출력
    global Ucount
    global Ccount
    userPhoto=PhotoImage(file="C:/Users/allab/Desktop/RSP/"+rspBig[userN])
    uLabel.configure(image=userPhoto)
    uLabel.image=userPhoto
    #컴퓨터 사진 출력
    comN=random.randrange(3)
    comPhoto=PhotoImage(file="C:/Users/allab/Desktop/RSP/"+rspBig[comN])
    cLabel.configure(image=comPhoto)
    cLabel.image=comPhoto
    #컴퓨터:n승 ,유저:n승 이겼습니다 출력
    if (userN+1)%3 == comN: #유저 패
        Ucount+=0
        Ccount+=1
        comResult.configure(text="computer:"+str(Ccount)+"승")
        userResult.configure(text="user:"+str(Ucount)+"승")
        ResultText.configure(text=result[1])
    elif userN == comN:
        Ucount+=0
        Ccount+=0
        comResult.configure(text="computer:"+str(Ccount)+"승")
        userResult.configure(text="user:"+str(Ucount)+"승")
        ResultText.configure(text=result[2])
    else:#유저 승
        Ucount+=1
        Ccount+=0
        comResult.configure(text="computer:"+str(Ccount)+"승")
        userResult.configure(text="user:"+str(Ucount)+"승")
        ResultText.configure(text=result[0])


##메인 코드 부분## 
window=Tk()
window.geometry("500x500")
window.resizable(width=FALSE,height=FALSE)

label1=Label(window,text="***가위바위보 게임***")
label2=Label(window,text="버튼을 선택하세요!",fg="red")


photoR=PhotoImage(file="C:/Users/allab/Desktop/RSP/"+rspList[1])#가위바위보 작은사진 저장해둠(바위 작은 사진)
photoS=PhotoImage(file="C:/Users/allab/Desktop/RSP/"+rspList[0])
photoP=PhotoImage(file="C:/Users/allab/Desktop/RSP/"+rspList[2])
btnR=Button(window,image=photoR,command=clickRock) #유저가 선택하는 버튼
btnS=Button(window,image=photoS,command=clickScissor)
btnP=Button(window,image=photoP,command=clickPaper)



comResult=Label(window,text='',fg="blue") #컴퓨터의 이긴 횟수가 나오는 텍스트
userResult=Label(window,text='',fg="green")#유저의 이긴 횟수가 나오는 텍스트
ResultText=Label(window,text="결과") #유저의 승패가 나오는 텍스트

userPhoto=PhotoImage() #유저가 선택할 사진 저장해두는 곳
comPhoto=PhotoImage() #컴퓨터가 선택할 사진 저장해주는 곳 
uLabel=Label(window,image='')#유저가 선택한 사진 레이블
cLabel=Label(window,image='')#컴퓨터가 선택한 사진 레이블


#위치시키기
label1.place(x=190,y=5)
label2.place(x=200,y=25)

btnR.place(x=80,y=45)
btnS.place(x=220,y=45)
btnP.place(x=360,y=45)

comResult.place(x=80,y=480)
userResult.place(x=350,y=480)
ResultText.place(x=220,y=480) 
uLabel.place(x=260,y=200) 
cLabel.place(x=30,y=200)

window.mainloop()
