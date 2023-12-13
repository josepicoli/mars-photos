from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

blue = "#0B3D91"
red = "#FC3D21"
white = "#FFFFFF"

#turn the URL into an image for tkinter
def load_image_from_url(url):
    response = requests.get(url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    return ImageTk.PhotoImage(img)

def show_image(rover, sol, camera, api_key):
    frame = Toplevel()
    frame.title("Photo")
    frame.geometry("1028x700")
    frame.config(bg= "#000000")
    frame.resizable(width= False, height= False)
    
    try:
        frame.iconbitmap("img\\favicon.ico")
    except:
        pass

    try:
        mars_rover_photos = requests.get(url= f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?sol={sol}&camera={camera}&api_key={api_key}")

        mars_rover_photos = mars_rover_photos.json()
        url_mars = mars_rover_photos["photos"][0]["img_src"]
        print(url_mars)

        photo = load_image_from_url(url_mars)

        img_mars = Label(frame, image= photo)
        img_mars.place(x= -2, y= -2)
    except:
        lb_error = Label(frame)
        lb_error.config(text= "image not found")
        lb_error.place(x= 0,y= 0)
        lb_error.config(width= 15, height= 1)
        lb_error.config(font= "Arial 20 bold")
        lb_error.config(fg= red, bg= blue)
        frame.config(bg= blue)

    frame.mainloop()

def show_help():
    frame = Toplevel()
    frame.geometry("350x160")
    frame.resizable(width= False, height= False)
    frame.title("Help")
    frame.config(background= blue)

    try:
        frame.iconbitmap("img\\favicon.ico")
    except:
        pass

    lb_help = Label(frame)
    lb_help.config(text= "Rover name and cameras name:")
    lb_help.place(x= 10, y= 10)
    lb_help.config(bg= blue, fg= white)
    lb_help.config(font= "Arial 15 bold")

    lb_Perseverance = Label(frame)
    lb_Perseverance.config(text= "Perseverance:")
    lb_Perseverance.place(x= 10, y= 40)
    lb_Perseverance.config(bg= blue, fg= white)
    lb_Perseverance.config(font= "Arial 15 bold")

    cb_Perseverance = ttk.Combobox(frame)
    Perseverance_cameras = ["Perseverance", "EDL_RUCAM", "EDL_RDCAM", "EDL_DDCAM", "EDL_PUCAM1", "EDL_PUCAM2", "NAVCAM_LEFT", "NAVCAM_RIGHT", "MCZ_RIGHT", "MCZ_LEFT", "FRONT_HAZCAM_LEFT_A", "FRONT_HAZCAM_RIGHT_A", "REAR_HAZCAM_LEFT", "REAR_HAZCAM_RIGHT", "SHERLOC_WATSON"]
    cb_Perseverance.set("Perseverance")
    cb_Perseverance.config(values= Perseverance_cameras)
    cb_Perseverance.place(x= 10, y= 70)

    lb_Curiosity = Label(frame)
    lb_Curiosity.config(text= "Curiosity:")
    lb_Curiosity.place(x= 160, y= 40)
    lb_Curiosity.config(bg= blue, fg= white)
    lb_Curiosity.config(font= "Arial 15 bold")

    cb_Curiosity = ttk.Combobox(frame)
    Curiosity_cameras = ["Curiosity", "FHAZ", "RHAZ", "MAST", "CHEMCAM", "MAHLI", "MARDI", "NAVCAM"]
    cb_Curiosity.set("Curiosity")
    cb_Curiosity.config(values= Curiosity_cameras)
    cb_Curiosity.place(x= 160, y= 70)

    lb_Opportunity= Label(frame)
    lb_Opportunity.config(text= "Opportunity:")
    lb_Opportunity.place(x= 10, y= 90)
    lb_Opportunity.config(bg= blue, fg= white)
    lb_Opportunity.config(font= "Arial 15 bold")

    cb_Opportunity = ttk.Combobox(frame)
    Opportunity_cameras = ["Opportunity", "FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"]
    cb_Opportunity.set("Opportunity")
    cb_Opportunity.config(values= Opportunity_cameras)
    cb_Opportunity.place(x= 10, y= 120)

    lb_Spirit= Label(frame)
    lb_Spirit.config(text= "Spirit:")
    lb_Spirit.place(x= 160, y= 90)
    lb_Spirit.config(bg= blue, fg= white)
    lb_Spirit.config(font= "Arial 15 bold")

    cb_Spirit = ttk.Combobox(frame)
    Spirit_cameras = ["Spirit", "FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"]
    cb_Spirit.set("Spirit")
    cb_Spirit.config(values= Spirit_cameras)
    cb_Spirit.place(x= 160, y= 120)

    frame.mainloop()

def main_interface():
    api_key = set_api_key()

    frame = Tk()
    frame.title("Mars Photos")
    frame.config(background= blue)
    frame.resizable(width= False, height= False)
    frame.geometry("400x200")
    
    try:
        frame.iconbitmap("img\\favicon.ico")
    except:
        print("favicon not found :3")

    lb_name_rover = Label(frame)
    lb_name_rover.config(text= "Rover name: ")
    lb_name_rover.place(x= 10,y= 15)
    lb_name_rover.config(width= 13, height= 1)
    lb_name_rover.config(font= "Arial 15 bold")
    lb_name_rover.config(fg= white, bg= blue)
    
    txt_name_rover = Entry(frame)
    txt_name_rover.config(width= 20)
    txt_name_rover.config(bg= white)
    txt_name_rover.config(bd= 0)
    txt_name_rover.config(font= "Arial 13")
    txt_name_rover.place(x= 150,y= 20)
    
    lb_sol = Label(frame)
    lb_sol.config(text= "Sol: ")
    lb_sol.place(x= 104,y= 45)
    lb_sol.config(width= 4, height= 1)
    lb_sol.config(font= "Arial 15 bold")
    lb_sol.config(fg= white, bg= blue)

    txt_sol = Entry(frame)
    txt_sol.config(width= 20)
    txt_sol.config(bg= white)
    txt_sol.config(bd= 0)
    txt_sol.config(font= "Arial 13")
    txt_sol.place(x= 150,y= 50)

    lb_camera = Label(frame)
    lb_camera.config(text= "Camera: ")
    lb_camera.place(x= 60,y= 74)
    lb_camera.config(width= 8, height= 1)
    lb_camera.config(font= "Arial 15 bold")
    lb_camera.config(fg= white, bg= blue)

    txt_camera = Entry(frame)
    txt_camera.config(width= 20)
    txt_camera.config(bg= white)
    txt_camera.config(bd= 0)
    txt_camera.config(font= "Arial 13")
    txt_camera.place(x= 150,y= 80)

    button_search = Button(frame)
    button_search.config(text= "Search")
    button_search.config(font= "Arial 15 bold")
    button_search.place(x= 150,y= 130)
    button_search.config(width= 10, height= 1)
    button_search.config(bg= red, fg= white)
    button_search.config(cursor="hand2")
    button_search.config(borderwidth=0)
    button_search.config(command= lambda: show_image(txt_name_rover.get(), txt_sol.get(), txt_camera.get(), api_key))

    button_help = Button(frame)
    button_help.config(text= "Help")
    button_help.config(font= "Arial 13 bold")
    button_help.config(bd = 0)
    button_help.config(borderwidth= 0)
    button_help.config(bg = red, fg = white)
    button_help.config(cursor= "hand2")
    button_help.place(x= 354, y= 172)
    button_help.config(command= show_help)

    frame.mainloop()

def set_api_key():
    try:
        with open("api_key.txt", "r") as key:
            key = key.read().strip()
            if key != "":
                print(repr(key))
                return key
        raise Exception()
    except:
        print(repr("DEMO_KEY"))
        return "DEMO_KEY"

main_interface()
