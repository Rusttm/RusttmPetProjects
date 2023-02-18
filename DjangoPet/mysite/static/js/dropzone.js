Dropzone.autoDiscover=false;
const myDropzone= new Dropzone('#my-dropzone',{
    url:'upload/',
    maxFiles:5,
    maxFilesize:5,
//    acceptedFiles: '.png,.jpg,.gif,.bmp,.jpeg',
    acceptedFiles:"image/jpeg,image/png,image/gif,image/jpg,application/pdf",
    acceptedMimeTypes: "audio/*,image/*,.psd,.pdf",
})