from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.card import MDCard
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.utils import platform
from kivy.metrics import dp
from kivymd.uix.button import MDIconButton
import webbrowser
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivymd.uix.button import MDFlatButton
from kivymd.uix.gridlayout import MDGridLayout
import yt_dlp
import threading
import os
from kivymd.uix.fitimage import FitImage
from kivymd.uix.list import OneLineAvatarIconListItem, MDList

from kivy.uix.scrollview import ScrollView
from kivymd.uix.dialog import MDDialog
class MyLogger:
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


class DownloadTextField(MDTextField):

    def on_touch_down(self, touch):

        if self.collide_point(*touch.pos):

            # icon area detect
            if self.icon_right and touch.x > self.right - dp(40):

                print("Download icon clicked")

                if hasattr(self, "download_function"):
                    self.download_function()

        return super().on_touch_down(touch)



class VideoDownloader(MDApp):
	#_____main___screen

    def build(self):

        #

        self.layout = MDBoxLayout(orientation="vertical",spacing=20,padding=20,md_bg_color = (1, 0.85, 0.88, 1))
        self.main_screen()
        return self.layout
    def main_screen(self):
    	
    
        self.screen = MDScreen()
        self.layout.clear_widgets()
        self.screen.clear_widgets()
        
    	
    	
        self.lbl=MDLabel(text="[u][b][size=50] LINK TUBE[/size][/b][/u]",markup=True,pos_hint={"center_x":0.5,"center_y":0.9},theme_text_color='Custom',text_color=(0, 0.6, 0, 1),)
        #_____instragram download card
        self.exit_btn=MDIconButton(icon="window-close",pos_hint={"center_x":0.9,"center_y":0.9},theme_icon_color='Custom',icon_color=(1,0,0,1),on_release=self.show_dialogue)
        
        self.card=MDCard(size_hint=(1,None),radius=[10]*4,elevation=1,md_bg_color = (1, 0.98, 0.9, 1),pos_hint={"center_x":0.5,"center_y":0.7},)
        
        
        

        

        self.link = DownloadTextField(
            hint_text=" Paste the video link here",
            size_hint_y=None,
            height="300dp",text_color_normal = (0,0,0,1),
        text_color_focus = (0,0,0,1),hint_text_color_normal = (0,0,0,1),
        hint_text_color_focus = (0,0,0,1),mode="line",size_hint=(1,None),pos_hint={"center_y":0.8,"center_x":0.5},icon_right="download",icon_right_color_focus=(0.7, 0.7, 0.7, 1),line_color_normal=(1, 0.85, 0.88, 1),line_color_focus=(1, 0.85, 0.88, 1)
        )
        self.link.download_function = lambda: self.start_download(None)
        self.war_cd=MDCard(size_hint=(1,None),height=dp(200),elevation=1,radius=[10]*4,pos_hint={"center_y":0.5,"center_x":0.5},md_bg_color = (1, 0.85, 0.88, 1))
        self.explain_lbl=MDLabel(text="  Paste the Instagram, \n  Facebook, or YouTube link \n  above\n\n  [color=#FF0000]NOTE :-[/color]Some videos may not be downloadable",size_hint=(1,None),bold=True,pos_hint={"center_y":0.6,},markup=True,halign="left")
        self.explain_lbl.bind(width=lambda instance,value:setattr(instance,'text_size',(value,None)),texture_size=lambda instance,value:setattr(instance,'height',value[1]))
        self.war_cd.add_widget(self.explain_lbl)
        self.more_btn=MDFlatButton(text='[b]More[/b]',theme_text_color='Custom',text_color=(1,0,0,1),pos_hint={"center_y":0.1,"center_x":0.7})
        self.war_cd.add_widget(self.more_btn)
        self.text = "Download audio"
        self.index = 0
        self.lb= MDLabel(text="",bold=True,halign="center",pos_hint={"center_y":0.3,"center_x":0.5})
        self.audio_btn=MDIconButton(icon="music-note",theme_icon_color="Custom",icon_color=(0,0,1,1),pos_hint={"center_y":0.3,"center_x":0.8},icon_size="25sp",on_release=self.audio_ui)
        
        self.screen.add_widget(self.audio_btn)
        
            
            
        
        Clock.schedule_interval(self.show_letter, 0.1)
        
        #______________________________


        #___ui__downloading..._______
        self.progress = MDProgressBar(
    value=0,
    color=(0,0.8,0.2,1),
    height="8dp",
    size_hint=(1,None),
    pos_hint={"center_x":0.5}
)
        
        self.status = MDLabel(
            text="Ready",bold=True,
            halign="center",markup=True,pos_hint={"center_x":0.3,"center_y":0.1}
        )
        self.icons_card=MDCard(size_hint=(0.4,None),height=dp(70),elevation=1,pos_hint={"center_x":0.8,"center_y":0.2},radius=[10]*4,md_bg_color = (1, 0.85, 0.88, 1))
        self.youtube_icon=MDIconButton(icon='youtube',theme_icon_color='Custom',icon_color=(1,0,0,1),pos_hint={"center_x":0.3,"center_y":0.5},on_release=self.open_youtube)
        self.icons_card.add_widget(self.youtube_icon)
        self.fb_icon=MDIconButton(icon='facebook',theme_icon_color='Custom',icon_color=(0,0,1,1),pos_hint={"center_x":0.5,"center_y":0.5},on_release=self.open_fb)
        self.icons_card.add_widget(self.fb_icon)
        self.inst_icon=MDIconButton(icon='instagram',theme_icon_color='Custom',icon_color=(1,0,0,1),pos_hint={"center_x":0.9,"center_y":0.5},on_release=self.open_instagram)
        #self.screen.add_widget(self.top_notification)
        
        self.icons_card.add_widget(self.inst_icon)

        self.screen.add_widget(self.lbl)
        self.screen.add_widget(self.exit_btn)
        
        self.screen.add_widget(self.link)
        self.screen.add_widget(self.war_cd)
        self.screen.add_widget(self.lb)
        self.screen.add_widget(self.icons_card)
        
        
        
        
        
        
        self.screen.add_widget(self.progress)
        
        self.screen.add_widget(self.status)

        self.layout.add_widget(self.screen)

        return self.layout
    
#________        

    def start_download(self, *args):
        url = self.link.text.strip()

        if not url:
            self.status.text = "Please paste the link"
            return

        self.status.text = "Downloading..."
        self.progress.value = 0

        threading.Thread(
            target=self.download_video,
            args=(url,),
            daemon=True
        ).start()

    def hook(self, d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded = d.get('downloaded_bytes', 0)

            if total:
                percent = downloaded / total * 100
                Clock.schedule_once(lambda dt: self.update_progress(percent))

        elif d['status'] == 'finished':
            Clock.schedule_once(lambda dt: self.finish_download())

    def update_progress(self, percent):
        self.progress.value = percent
        self.status.text = f"Downloading... {int(percent)}%"

    def finish_download(self):
        self.progress.value = 100
        self.status.text = "Download Complete "

    def download_video(self, url):

        download_path = "/storage/emulated/0/Download/"

        ydl_opts = {
            "outtmpl": download_path + "%(title)s.%(ext)s",

            # ✅ FIXED (No ffmpeg needed)
            "format": "best",

            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
            "retries": 10,
            "fragment_retries": 10,

            "logger": MyLogger(),
            "progress_hooks": [self.hook],

            "http_headers": {
                "User-Agent": "Mozilla/5.0"
            }
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        except Exception as e:
            Clock.schedule_once(lambda dt, err=str(e): self.error(err))

    def error(self, msg):
        self.status.text = f"Error: {msg}"


                                                   
  
        
    
        
#_________
        
    def  show_dialogue(self,instance):
    	self.dialog = MDDialog(
        
        text="Do you want to exit the app?",
        buttons=[
            MDFlatButton(
                text="[b]NO[/b]",
                on_release=lambda x:self.dialog.dismiss(x),theme_text_color='Custom',text_color=(0,0,1,1)
            ),
            MDFlatButton(
                text="[b]EXIT[/b]",theme_text_color='Custom',text_color=(1,0,1,1),
                on_release=lambda x:self.stop(x)
            ),
        ],
   radius=[10]*4,md_bg_color = (1, 0.85, 0.88, 1))
    	self.dialog.open()
    	
    
    def open_youtube(self, instance):
        webbrowser.open("https://www.youtube.com")                
                	
    def open_instagram(self, instance):
        webbrowser.open("https://www.instagram.com")               
    def open_fb(self, instance):
        webbrowser.open("https://www.facebook.com")
        
    def show_letter(self, dt):
    	if self.index < len(self.text):
    		self.lb.text += self.text[self.index]
    		self.index += 1
    	else:
    		self.index = 0
    		self.lb.text = ""

    	
    def audio_ui(self,instance):
     	self.screen.clear_widgets()
     	#self.layout.clear_widgets()
     	self.audio_lbl=MDLabel(text="[u][b][size=50] LINK TUBE[/size][/b][/u]",markup=True,pos_hint={"center_x":0.5,"center_y":0.9},theme_text_color='Custom',text_color=(0, 0,1, 1),)
     	self.aud_exit_btn=MDIconButton(icon="arrow-right-bold",pos_hint={"center_x":0.9,"center_y":0.9},theme_icon_color='Custom',icon_color=(0,0,1,1),on_release=lambda x:self.main_screen())
     	self.aud_card=MDCard(size_hint=(1,None),radius=[10]*4,elevation=1,md_bg_color = (1, 0.98, 0.9, 1),pos_hint={"center_x":0.5,"center_y":0.7},)
     	self.aud_link = DownloadTextField(
            hint_text=" Paste  audio link here",size_hint_y=None,height="300dp",text_color_normal = (0,0,0,1),text_color_focus = (0,0,0,1),hint_text_color_normal = (0,0,0,1),
hint_text_color_focus = (0,0,0,1),mode="line",size_hint=(1,None),pos_hint={"center_y":0.8,"center_x":0.5},icon_right="download",icon_right_color_focus=(0.7, 0.7, 0.7, 1),line_color_normal=(1, 0.85, 0.88, 1),line_color_focus=(1, 0.85, 0.88, 1))
#
     	self.aud_link.download_function = lambda: self.start_audio_download(None)
     	self.aud_war_cd=MDCard(size_hint=(1,None),height=dp(200),elevation=1,radius=[10]*4,pos_hint={"center_y":0.5,"center_x":0.5},md_bg_color = (1, 0.85, 0.88, 1))
     	self.aud_explain_lbl=MDLabel(text="  Paste the Instagram, \n  Facebook, or YouTube link \n  above\n\n  [color=#FF0000]NOTE :[/color]Some audio files may not be downloadable",size_hint=(1,None),bold=True,pos_hint={"center_y":0.6,},markup=True,halign="left")
     	#
     	self.aud_explain_lbl.bind(width=lambda instance,value:setattr(instance,'text_size',(value,None)),texture_size=lambda instance,value:setattr(instance,'height',value[1]))
     	self.aud_war_cd.add_widget(self.aud_explain_lbl)
     	self.aud_more_btn=MDFlatButton(text='[b]more[/b]',theme_text_color='Custom',text_color=(1,0,0,1),pos_hint={"center_y":0.1,"center_x":0.7})
     	self.aud_war_cd.add_widget(self.aud_more_btn)
     	#self.aud_text = "Download audio"
     	#self.index = 0
     	#self.aud_lb= MDLabel(text="",bold=True,halign="center",pos_hint={"center_y":0.3,"center_x":0.5})
     	#self.audio_btn=MDIconButton(icon="music-note",theme_icon_color="Custom",icon_color=(0,0,1,1),pos_hint={"center_y":0.3,"center_x":0.8},icon_size="25sp")
     	#self.screen.add_widget(self.audio_btn)
     	#Clock.schedule_interval(self.show_letter, 0.1)
     	#self.aud_progress=MDProgressBar(value=0,color=(0,0.8,0.2,1),height="8dp",size_hint=(1,None),pos_hint={"center_x":0.5})
     	self.aud_status = MDLabel(text="Status: Waiting...",bold=True,halign="center",markup=True,pos_hint={"center_x":0.3,"center_y":0.1})
     	self.aud_icons_card=MDCard(size_hint=(0.4,None),height=dp(70),elevation=1,pos_hint={"center_x":0.8,"center_y":0.2},radius=[10]*4,md_bg_color = (1, 0.85, 0.88, 1))
     	self.aud_youtube_icon=MDIconButton(icon='youtube',theme_icon_color='Custom',icon_color=(1,0,0,1),pos_hint={"center_x":0.3,"center_y":0.5},on_release=self.open_youtube)
     	self.aud_icons_card.add_widget(self.aud_youtube_icon)
     	self.aud_fb_icon=MDIconButton(icon='facebook',theme_icon_color='Custom',icon_color=(0,0,1,1),pos_hint={"center_x":0.5,"center_y":0.5},on_release=self.open_fb)
     	self.aud_icons_card.add_widget(self.aud_fb_icon)
     	self.aud_inst_icon=MDIconButton(icon='instagram',theme_icon_color='Custom',icon_color=(1,0,0,1),pos_hint={"center_x":0.9,"center_y":0.5},on_release=self.open_instagram)
     	self.aud_icons_card.add_widget(self.aud_inst_icon)
     	self.screen.add_widget(self.audio_lbl)
     	self.screen.add_widget(self.aud_exit_btn)
     	self.screen.add_widget(self.aud_link)
     	self.screen.add_widget(self.aud_war_cd)
     	self.screen.add_widget(self.aud_status)
     	self.screen.add_widget(self.aud_icons_card)
     	#self.screen.add_widget(self.aud_progress)
     	#__________



    def start_audio_download(self, instance):
        threading.Thread(target=self.download_audio, daemon=True).start()


    def update_status(self, msg):
        Clock.schedule_once(lambda dt: setattr(self.aud_status, 'text', msg))


    def download_audio(self):
        url = self.aud_link.text.strip()

        if not url:
            self.update_status("Paste the audio link")
            return

        self.update_status("Downloading...")

        download_path = "/storage/emulated/0/Download/"

        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": download_path + "%(title)s.%(ext)s",
            "quiet": True,
            "no_warnings": True,
            "noplaylist": True,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.update_status("✅ Download Complete")

        except Exception as e:
            self.update_status("❌ Error: " + str(e))                            
VideoDownloader().run()
