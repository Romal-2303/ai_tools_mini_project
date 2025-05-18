import yt_dlp

def get_video_info(youtube_url: str):
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'simulate': True,
            'extract_flat': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            
            # Get the best quality mp4 format
            formats = [f for f in info['formats'] if f['ext'] == 'mp4' and f.get('filesize')]
            if not formats:
                return {"error": "No MP4 format available"}
                
            best_format = max(formats, key=lambda x: x.get('width', 0))
            
            return {
                "duration": info['duration'],
                "format": 'mp4',
                "size": best_format['filesize'] // (1024 * 1024) if best_format.get('filesize') else 0
            }
            
    except Exception as e:
        return {"error": str(e)}