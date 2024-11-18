from pytubefix import YouTube
import instaloader

def do_yt(self, line):
    line = line.split()
    if line[0] == 'mp3':
        try:
            link = line
            yt = YouTube(link[1])
            yt.streams.get_audio_only().download()
            print("Downloaded mp3")
        
        except Exception as e:
            print(e)
    elif line[0] == 'mp4':     
        try:
            link = line
            yt = YouTube(link[1])
            yt.streams.get_highest_resolution().download()
            print("Downloaded mp4")
        
        except Exception as e:
            print(e)
    else:
        print(f"Invalid format ({line[0]}). Use 'mp3' or 'mp4' then the link (e.g. yt mp3 https://www.youtube.com/watch)")

def do_ig(self, line):
    try:
        insta = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(insta.context, line.split('/')[-2])
        insta.download_post(post, target=post.shortcode)
        print("Downloaded post")
    except Exception as e:
        print(e)
