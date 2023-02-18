def handle_uploaded_file(f):
    print('start to uploading...')
    with open('files/uploaded_file.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)