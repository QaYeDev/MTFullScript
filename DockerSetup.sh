#!/bin/bash

# Install Docker
sudo apt-get update
sudo apt-get install -y docker.io

# Install QEMU and some tools for windows support
sudo apt-get install apt-utils -y
sudo apt-get install -y vagrant qemu qemu-user-static binfmt-support qemu-kvm libvirt-daemon-system libvirt-dev

# Download Windows Server Core image
docker pull mcr.microsoft.com/windows/servercore:ltsc2022-amd64

# Create Docker volume for QEMU
docker volume create qemu

# Mount the QEMU binary in the Docker volume
docker run --rm --privileged multiarch/qemu-user-static:register --reset

# Run the Windows Server Core container with QEMU
docker run --rm -it --platform=windows -v qemu:/usr/bin/qemu:ro mcr.microsoft.com/windows/servercore:ltsc2022-amd64 powershell













#!/bin/bash

# تثبيت Docker
sudo apt-get -y install docker.io

# تنزيل صورة Debian
sudo docker pull debian

#إنشاء المساحة للحاوية
#docker volume create mydata

# إنشاء ملف dockerfile
echo "FROM qayedev/mydata" > dockerfile
echo "WORKDIR /data" >> dockerfile
echo "RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y dialog && apt-get install -y xrdp" >> dockerfile
echo "EXPOSE 33389" >> dockerfile
#echo 'CMD ["xrdp", "--nodaemon"]' >> dockerfile

# بناء الحاوية
sudo docker build -t mydata -f dockerfile .


# تصدير الحاوية
sudo docker save -o mydata.tar mydata

# تحميل الحاوية وتشغيلها
sudo docker load -i mydata.tar
docker run -it --name mydata mydata
#حفظ التغييرات الجديدة بعد الخروج.
sudo docker commit mydata
# تصدير الحاوية بعد إجراء التغييرات.
sudo docker save -o mydata.tar mydata

#sudo docker run -p 33389:33389 mydata



ضبط المستودع الخارجي.
docker login -username=qayedev --password=C?gq4jN!EXn*De^

#إنشاء المستودع إن كان غير موجود للحاوية
docker tag mydata qayedev/mydata

#تحديث الحاوية
docker push qayedev/mydata

#تنزيل الحاوية من المستودع
docker pull qayedev/mydata

#تشغيل الحاوية من المستودع
docker run -it --name mydata qayedev/mydata

#حفظ التغييرات بعد الخروج
docker commit mydata qayedev/mydata

#تحديث الحاوية إلى المستودع بعد التغييرات 
docker push qayedev/mydata

#إيقاف وإزالة الحاوية عند الإنتهاء
