# files-to-image-conversion-v2
Convert any types of files into color or grayscale images

- This is a better version of the previous program.
- Previous program was web based so there were certain limitation on the total number of files for processing and also restriction on access of local file system of the user
- This program is only API based
- You have to provide the path of the input directory where files are located and output directory where you want to save the images
- It also requires the value of mode, image format, image size and resampling filter while making a request to the API endpoint
- There are no limit to the no. of files one folder should have
- This program process the files one by one in a sequential manner so no worries for memory problem

  ## Here is how your request should look like:
  Endpoint: http://127.0.0.1:8000/convert

  Body:
```
  {
      "input_dir": "",
      "output_dir": "",
      "mode": "grayscale",
      "imgFormat": "png",
      "imageSize": 256,
      "resampling_filter": "BICUBIC"
  }
```

- mode: "color" or "grayscale"
- imgFormat: "png" or "jpeg"
- imageSize: 128 or 256 or any value
- You can also use different resampling filter apart from the mentioned one to resize the image

## Usecase of this program
- You can use this to prepare the image dataset for CNN model

## Future TODO
- I have not tested this program for the limit of one file size
- The dataset I am preparing right now has no such requirements but surely, I will test this for the single file size limit
- Idealy, when processing a single file that file is read byte by byte and the values are stored in a numpy array so if the file size is too large then the array will also be too large and it will require more memory
- One approach would be to split the file into parts if it is too large and process each part at a time and after processing all the parts we can combine the result
- But, this may has some issues...Anyway, I will tackle that some other time
