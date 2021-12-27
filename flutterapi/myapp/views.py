from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from .serializers import TodolistSerializer
from .models import Todolist

#get data
@api_view(['GET'])
def all_todolist(request):
    alltodolist = Todolist.objects.all() #ดึงข้อมูลจาก model Todolist 
    serializer = TodolistSerializer(alltodolist,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

#POST data (save data to database)
@api_view(['POST'])
def post_todolist(request):
    if request.method == 'POST':
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_todolist(request,TID):
    #localhist:8000/api/update-todolist/TID
    todo = Todolist.objects.get(id=TID)

    if request.method == 'PUT':
        data ={}
        serializers=TodolistSerializer(todo,data=request.data)
        if serializers.is_valid():
            serializers.save()
            data['status']='updated'
            return Response(data=data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_todolist(request,TID):
    todo = Todolist.objects.get(id=TID)

    if request.method == 'DELETE':
        delete =todo.delete()
        data={}
        if delete:
            data['status']='delete'
            statuscode = status.HTTP_200_OK
        else:
            data['status']='failed'
            statuscode = status.HTTP_400_BAD_REQUEST

        return Response(data=data, status=statuscode)

data = [
    {
        "title":"What's the Medical Device ? ",
        "subtitle":"Medical Device คือ อุปกรณ์ที่ใช้ในทาการแพทย์... ",
        "image_url":"https://raw.githubusercontent.com/banditphiboon/BasicAPI/main/ct-scan-6506418_960_720.jpg",
        "detail":"ของใช้ประจำอยู่กับเครื่องมือแพทย์เป็นอาจิณเพื่อประโยชน์แก่การจัดดูแล ใช้สอย หรือรักษาเครื่องมือแพทย์\nเครื่องใช้ ผลิตภัณฑ์ หรือวัตถุอื่นที่รัฐมนตรีประกาศกำหนดในราชกิจจานุเบกษาว่าเป็นเครื่องมือแพทย์"

    },
    {
        "title":"Type of Medical Device ?",
        "subtitle":"ประภทของเครื่องมือมีหลายประเภท...",
        "image_url":"https://raw.githubusercontent.com/banditphiboon/BasicAPI/main/scalpel-5800533_960_720.jpg",
        "detail":"เครื่อง มือแพทย์นั้นแบ่งได้เป็น 4 ประเภทใหญ่ ๆ ด้วยกัน คือ\n1. อุปกรณ์ผ่าตัด และอุปกรณ์การแพทย์ เช่น มีดผ่าตัด กรรไกรผ่าตัด เครื่องวัดความดัน ปรอท วัดไข้ เป็นต้น\n2. บริภัณฑ์การแพทย์ เช่น เครื่องเอกซเรย์ เครื่องอัลตราซาวด์ เครื่องสลายนิ่ว เป็นต้น\n3. วัสดุการแพทย์และวัสดุฝังในทางศัลยกรรม เช่น ถุงมือยางทางการแพทย์ ผ้าก๊อซ ซิลิโคน(Silicone)\n4. เครื่องมือแพทย์เฉพาะทาง เช่น ชุดน้ำยาตรวจการติดเชื้อ เอชไอวี (HIV) ชุดตรวจน้ำตาล ในปัสสาวะ เครื่องมือทันตกรรม เป็นต้น\n"
    },
    {
        "title":"What's the medical device standard ?",
        "subtitle":"มาตราฐานเครื่องมือแพทย์ต้องได้รับ...",
        "image_url":"https://raw.githubusercontent.com/banditphiboon/BasicAPI/main/pulse-oximeter-6331691_960_720.jpg",
        "detail":"มาตรฐาน ISO 13485 เป็นมาตรฐานที่พัฒนาขึ้น เพื่อเป็นแนวทางในการพัฒนาระบบบริหารคุณภาพ สำหรับองค์กรที่เกี่ยวกับเครื่องมือแพทย์ ครอบคลุมตั้งแต่ การออกแบบ การผลิต การขาย การติดตั้ง และการบริการ โดยมีเป้าหมายเพื่อให้ผลิตเครื่องมือแพทย์ที่มีคุณภาพ และปลอดภัยกับผู้ใช้งาน ประกาศใช้ครั้งแรก เมื่อปี 1996 ภายหลังจากที่มีการออกมาตรฐาน ISO9001 ฉบับปี 1994 โดยเนื้อหาข้อกำหนดของมาตรฐาน ISO 13485 จะครอบคลุมในส่วนของมาตรฐาน ISO 9001 ด้วย และเมื่อมาตรฐาน ISO9001 ได้มีการพัฒนามาเป็นฉบับปี 2000 มาตรฐาน ISO 13485 ก็ได้พัฒนาขึ้นมาเป็นฉบับปี 2003 ซึ่งในปัจจุบันยังไม่ได้มีการประกาศใช้ฉบับใหม่ ถึงแม้ว่ามาตรฐาน  ISO 9001 ได้มีการออกฉบับใหม่แล้วเป็นฉบับปี 2008 ก็ตามหากย้อนกลับไปในช่วงที่มีการออกมาตรฐาน ISO 9001 ฉบับปี 1994 ได้มีการพัฒนามาตรฐานที่เกี่ยวกับเครื่องมือแพทย์โดยเป็นการพัฒนาต่อยอดจากมาตรฐาน ISO 9001 ฉบับดังกล่าว ที่เรียกว่า EN46001 (European Norm) สำหรับผู้ผลิเครื่องมือแพทย์ที่จัดจำหน่ายในสหภาพยุโรป ซึ่งภายหลังจากที่มีการออกมาตรฐาน ISO 13485 แล้ว บริษัทต่างๆ ก็เปลี่ยนมาดำเนินการและรับรองมาตรฐาน ISO 13485 เป็นส่วนใหญ่"
    }

]

def Home(request):
    return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii':False})
