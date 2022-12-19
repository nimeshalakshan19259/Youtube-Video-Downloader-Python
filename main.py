from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("The entered link is not valied")
  print("video downloaded")

link = input("Paste your Link here! URL:")
Download(link)
  
  
  