from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO

BLUE = "#0B3D91"
RED = "#FC3D21"
WHITE = "#FFFFFF"

#turn the URL into an image for tkinter
def load_image_from_url(url :str):
    response = requests.get(url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    return ImageTk.PhotoImage(img)

def request(rover :str, sol :str, camera :str, API_KEY :str) -> list:
    try:
        r = requests.get(
        url= f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?sol={sol}&camera={camera}&api_key={API_KEY}"
        )

        return [i["img_src"] for i in r.json()["photos"]]
    except:
        return []

def show_image(indx_image :int, url_list :list):
    frame = Toplevel()
    frame.title('Photo')
    frame.geometry('1200x874')
    frame.config(bg= '#000000')
    frame.resizable(width= True, height= True)

    if indx_image < 0 or indx_image > len(url_list) - 1:
        lb_error = Label(frame)
        lb_error.config(text= 'image not found')
        lb_error.place(x= 0,y= 0)
        lb_error.config(width= 15, height= 1)
        lb_error.config(font= 'Arial 20 bold')
        lb_error.config(fg= RED, bg= BLUE)
        frame.config(bg= BLUE)

        frame.mainloop()

    photo = load_image_from_url(url_list[indx_image])
    img_mars = Label(frame, image = photo)
    img_mars.place(x = 0, y = 0)

    frame.mainloop()

def window_images(url_list :list):
    frame = Toplevel()
    frame.title('Photos')
    frame.geometry('400x250')
    frame.config(bg= BLUE)
    frame.resizable(width= False, height= False)

    if url_list == []:
        lb_error = Label(frame)
        lb_error.config(text= 'images not found')
        lb_error.place(x= 0,y= 0)
        lb_error.config(width= 15, height= 1)
        lb_error.config(font= 'Arial 20 bold')
        lb_error.config(fg= RED, bg= BLUE)
        frame.config(bg= BLUE)

        frame.mainloop()

    lb_show = Label(frame)
    lb_show.config(text= f'0 - {len(url_list) - 1}')
    lb_show.place(x= 125, y= 55)
    lb_show.config(font= 'Arial 16 bold')
    lb_show.config(fg= WHITE, bg= BLUE)
    lb_show.config(width= 12, height= 1)

    txt_show = Entry(frame)
    txt_show.config(width= 12)
    txt_show.config(bg= WHITE)
    txt_show.config(bd= 0)
    txt_show.config(font= 'Arial 16 bold')
    txt_show.place(x= 125,y= 90)

    button_show = Button(frame)
    button_show.config(text = 'show')
    button_show.config(font= 'Arial 13 bold')
    button_show.config(bd = 0)
    button_show.config(borderwidth= 0)
    button_show.config(bg = RED, fg = WHITE)
    button_show.config(cursor = 'hand2')
    button_show.place(x = 125, y = 130)
    button_show.config(width= 12, height= 1)
    button_show.config(command = lambda: show_image(int(txt_show.get()), url_list))

    frame.mainloop()

def create_website(url_list :list):
    if url_list == []:
        print('empty list, site not created')
        return
    
    START = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Mars Photos</title><style>body{background-color:black;}img{display:block;width:800px;margin-left:auto;margin-right:auto;margin-bottom:30px;}</style></head><body>\n'
    END = '</body></html>\n'
    with open('index.html', 'w') as site:
        site.write(START)
        for i in url_list:
            site.write(f'<img src="{i}">\n')
        site.write(END)
    print('site created')

def show_help():
    frame = Toplevel()
    frame.geometry("400x160")
    frame.resizable(width= False, height= False)
    frame.title("Help")
    frame.config(background= BLUE)

    lb_help = Label(frame)
    lb_help.config(text= "Rover name and cameras name:")
    lb_help.place(x= 10, y= 10)
    lb_help.config(bg= BLUE, fg= WHITE)
    lb_help.config(font= "Arial 15 bold")

    lb_Perseverance = Label(frame)
    lb_Perseverance.config(text= "Perseverance:")
    lb_Perseverance.place(x= 10, y= 40)
    lb_Perseverance.config(bg= BLUE, fg= WHITE)
    lb_Perseverance.config(font= "Arial 15 bold")

    cb_Perseverance = ttk.Combobox(frame)
    Perseverance_cameras = ["Perseverance", "EDL_RUCAM", "EDL_RDCAM", "EDL_DDCAM", "EDL_PUCAM1", "EDL_PUCAM2", "NAVCAM_LEFT", "NAVCAM_RIGHT", "MCZ_RIGHT", "MCZ_LEFT", "FRONT_HAZCAM_LEFT_A", "FRONT_HAZCAM_RIGHT_A", "REAR_HAZCAM_LEFT", "REAR_HAZCAM_RIGHT", "SHERLOC_WATSON"]
    cb_Perseverance.set("Perseverance")
    cb_Perseverance.config(values= Perseverance_cameras)
    cb_Perseverance.place(x= 10, y= 70)

    lb_Curiosity = Label(frame)
    lb_Curiosity.config(text= "Curiosity:")
    lb_Curiosity.place(x= 200, y= 40)
    lb_Curiosity.config(bg= BLUE, fg= WHITE)
    lb_Curiosity.config(font= "Arial 15 bold")

    cb_Curiosity = ttk.Combobox(frame)
    Curiosity_cameras = ["Curiosity", "FHAZ", "RHAZ", "MAST", "CHEMCAM", "MAHLI", "MARDI", "NAVCAM"]
    cb_Curiosity.set("Curiosity")
    cb_Curiosity.config(values= Curiosity_cameras)
    cb_Curiosity.place(x= 200, y= 70)

    lb_Opportunity= Label(frame)
    lb_Opportunity.config(text= "Opportunity:")
    lb_Opportunity.place(x= 10, y= 90)
    lb_Opportunity.config(bg= BLUE, fg= WHITE)
    lb_Opportunity.config(font= "Arial 15 bold")

    cb_Opportunity = ttk.Combobox(frame)
    Opportunity_cameras = ["Opportunity", "FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"]
    cb_Opportunity.set("Opportunity")
    cb_Opportunity.config(values= Opportunity_cameras)
    cb_Opportunity.place(x= 10, y= 120)

    lb_Spirit= Label(frame)
    lb_Spirit.config(text= "Spirit:")
    lb_Spirit.place(x= 200, y= 90)
    lb_Spirit.config(bg= BLUE, fg= WHITE)
    lb_Spirit.config(font= "Arial 15 bold")

    cb_Spirit = ttk.Combobox(frame)
    Spirit_cameras = ["Spirit", "FHAZ", "RHAZ", "NAVCAM", "PANCAM", "MINITES"]
    cb_Spirit.set("Spirit")
    cb_Spirit.config(values= Spirit_cameras)
    cb_Spirit.place(x= 200, y= 120)

    frame.mainloop()

def set_api_key():
    try:
        with open('api_key.txt', 'r') as key:
            key = key.read().strip()
            if key != '':
                print(f'key: {key}')
                return key
            raise Exception()
    except:
        print('key: DEMO_KEY')
        return 'DEMO_KEY'

def main_interface():
    API_KEY = set_api_key()

    frame = Tk()
    frame.title("Mars Photos")
    frame.config(background= BLUE)
    frame.resizable(width= False, height= False)
    frame.geometry("400x250")

    lb_name_rover = Label(frame)
    lb_name_rover.config(text= "Rover name: ")
    lb_name_rover.place(x= 10,y= 15)
    lb_name_rover.config(width= 13, height= 1)
    lb_name_rover.config(font= "Arial 15 bold")
    lb_name_rover.config(fg= WHITE, bg= BLUE)
    
    txt_show = Entry(frame)
    txt_show.config(width= 20)
    txt_show.config(bg= WHITE)
    txt_show.config(bd= 0)
    txt_show.config(font= "Arial 13")
    txt_show.place(x= 150,y= 20)
    
    lb_sol = Label(frame)
    lb_sol.config(text= "Sol: ")
    lb_sol.place(x= 104,y= 45)
    lb_sol.config(width= 4, height= 1)
    lb_sol.config(font= "Arial 15 bold")
    lb_sol.config(fg= WHITE, bg= BLUE)

    txt_sol = Entry(frame)
    txt_sol.config(width= 20)
    txt_sol.config(bg= WHITE)
    txt_sol.config(bd= 0)
    txt_sol.config(font= "Arial 13")
    txt_sol.place(x= 150,y= 50)

    lb_camera = Label(frame)
    lb_camera.config(text= "Camera: ")
    lb_camera.place(x= 60,y= 74)
    lb_camera.config(width= 8, height= 1)
    lb_camera.config(font= "Arial 15 bold")
    lb_camera.config(fg= WHITE, bg= BLUE)

    txt_camera = Entry(frame)
    txt_camera.config(width= 20)
    txt_camera.config(bg= WHITE)
    txt_camera.config(bd= 0)
    txt_camera.config(font= "Arial 13")
    txt_camera.place(x= 150,y= 80)

    button_search = Button(frame)
    button_search.config(text= "Search")
    button_search.config(font= "Arial 15 bold")
    button_search.place(x= 150,y= 130)
    button_search.config(width= 12, height= 1)
    button_search.config(bg= RED, fg= WHITE)
    button_search.config(cursor="hand2")
    button_search.config(borderwidth=0)
    button_search.config(command= lambda: 
        window_images(request(txt_show.get(), txt_sol.get(), txt_camera.get(), API_KEY))
    )
    
    button_site = Button(frame)
    button_site.config(text= "Create Website")
    button_site.config(font= "Arial 15 bold")
    button_site.place(x= 150,y= 170)
    button_site.config(width= 12, height= 1)
    button_site.config(bg= RED, fg= WHITE)
    button_site.config(cursor="hand2")
    button_site.config(borderwidth=0)
    button_site.config(command = lambda: 
        create_website(request(txt_show.get(), txt_sol.get(), txt_camera.get(), API_KEY))
    )

    button_help = Button(frame)
    button_help.config(text= "Help")
    button_help.config(font= "Arial 15 bold")
    button_help.config(bd = 0)
    button_help.config(borderwidth= 0)
    button_help.config(bg = RED, fg = WHITE)
    button_help.config(cursor= "hand2")
    button_help.place(x= 150, y= 210)
    button_help.config(width= 12, height= 1)
    button_help.config(command= show_help)

    frame.mainloop()

main_interface()