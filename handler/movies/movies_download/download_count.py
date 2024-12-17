from services.services import updateDownloadCount



def update_download_count_view(request, movie_code):
    download_count = updateDownloadCount(movie_code)

    data = {"download_count": download_count}
    
    return data
