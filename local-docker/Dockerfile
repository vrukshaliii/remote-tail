# Get the latest base image for python
FROM python:latest
# Put files at the image '/server/' folder.
ADD server.py /server/
# '/server/' is base directory
WORKDIR /server/
# Expose port 6677 in the container
EXPOSE 6677
# execute the command
CMD [ "python3", "/server/server.py" ]