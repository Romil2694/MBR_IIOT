from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserRegistrationForm
from django.http import HttpResponse
from django.contrib import messages


from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return HttpResponse("Hello MBR.")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            #messages.error(request,"Username or Password is incorrect")
            return HttpResponse("Username or password is incorrect.")
        login(request, user)
        messages.info(request, "You have logged in successfully!")
        return redirect("els")
    else:
        form = UserForm()
    return render(request, 'kohli_els/login.html', {'form': form})

def plcdata(request):
    data = {}
    datacollector = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="mbr"
    )
    mydata = datacollector.cursor()
    mydata.execute("SELECT * FROM kohli_els")
    dataarray = mydata.fetchall()
    realdata = dataarray[0]
    M_UW1_ACT_DIA = realdata[1]
    data['UW1_ACT_DIA'] = M_UW1_ACT_DIA
    M_UW2_ACT_DIA = realdata[2]
    data['UW2_ACT_DIA'] = M_UW2_ACT_DIA
    M_RW1_ACT_DIA = realdata[3]
    data['RW1_ACT_DIA'] = M_RW1_ACT_DIA
    M_RW2_ACT_DIA = realdata[4]
    data['RW2_ACT_DIA'] = M_RW2_ACT_DIA
    M_RW1_LENGTH = realdata[5]
    data['RW1_LENGTH'] = M_RW1_LENGTH
    M_RW2_LENGTH = realdata[6]
    data['RW2_LENGTH'] = M_RW2_LENGTH
    M_TOTAL_LENGTH = realdata[7]
    data['TOTAL_LENGTH'] = M_TOTAL_LENGTH
    M_UW_ACT_DANCER = realdata[8]
    data['UW_ACT_DANCER'] = M_UW_ACT_DANCER
    M_RW_ACT_DANCER = realdata[9]
    data['RW_ACT_DANCER'] = M_RW_ACT_DANCER
    M_INFEED_ACT_DANCER = realdata[10]
    data['INFEED_ACT_DANCER'] = M_INFEED_ACT_DANCER
    M_OUTFEED_ACT_DANCER = realdata[11]
    data['OUTFEED_ACT_DANCER'] = M_OUTFEED_ACT_DANCER
    M_PRINT_REPEAT = realdata[12]
    data['PRINT_REPEAT'] = M_PRINT_REPEAT
    M_PU1_ACT_TEMP = realdata[13]
    data['PU1_ACT_TEMP'] = M_PU1_ACT_TEMP
    M_PU2_ACT_TEMP = realdata[14]
    data['PU2_ACT_TEMP'] = M_PU2_ACT_TEMP
    M_PU3_ACT_TEMP = realdata[15]
    data['PU3_ACT_TEMP'] = M_PU3_ACT_TEMP
    M_PU4_ACT_TEMP = realdata[16]
    data['PU4_ACT_TEMP'] = M_PU4_ACT_TEMP
    M_PU5_ACT_TEMP = realdata[17]
    data['PU5_ACT_TEMP'] = M_PU5_ACT_TEMP
    M_PU6_ACT_TEMP = realdata[18]
    data['PU6_ACT_TEMP'] = M_PU6_ACT_TEMP
    M_PU7_ACT_TEMP = realdata[19]
    data['PU7_ACT_TEMP'] = M_PU7_ACT_TEMP
    M_PU8_ACT_TEMP = realdata[20]
    data['M_PU8_ACT_TEMP'] = M_PU8_ACT_TEMP
    M_PU9_ACT_TEMP = realdata[21]
    data['PU9_ACT_TEMP'] = M_PU9_ACT_TEMP
    M_PU10_ACT_TEMP = realdata[22]
    data['PU10_ACT_TEMP'] = M_PU10_ACT_TEMP
    M_UW1_FAULTCODE = realdata[23]
    data['UW1_FAULTCODE'] = M_UW1_FAULTCODE
    M_UW2_FAULTCODE = realdata[24]
    data['UW2_FAULTCODE'] = M_UW2_FAULTCODE
    M_RW1_FAULTCODE = realdata[25]
    data['RW1_FAULTCODE'] = M_RW1_FAULTCODE
    M_RW2_FAULTCODE = realdata[26]
    data['RW2_FAULTCODE'] = M_RW2_FAULTCODE
    M_INFEED_FAULTCODE = realdata[27]
    data['INFEED_FAULTCODE'] = M_INFEED_FAULTCODE
    M_OUTFEED_FAULTCODE = realdata[28]
    data['OUTFEED_FAULTCODE'] = M_OUTFEED_FAULTCODE
    M_PU1_FAULTCODE = realdata[29]
    data['PU1_FAULTCODE'] = M_PU1_FAULTCODE
    M_PU2_FAULTCODE = realdata[30]
    data['PU2_FAULTCODE'] = M_PU2_FAULTCODE
    M_PU3_FAULTCODE = realdata[31]
    data['PU3_FAULTCODE'] = M_PU3_FAULTCODE
    M_PU4_FAULTCODE = realdata[32]
    data['PU4_FAULTCODE'] = M_PU4_FAULTCODE
    M_PU5_FAULTCODE = realdata[33]
    data['PU5_FAULTCODE'] = M_PU5_FAULTCODE
    M_PU6_FAULTCODE = realdata[34]
    data['PU6_FAULTCODE'] = M_PU6_FAULTCODE
    M_PU7_FAULTCODE = realdata[35]
    data['PU7_FAULTCODE'] = M_PU7_FAULTCODE
    M_PU8_FAULTCODE = realdata[36]
    data['PU8_FAULTCODE'] = M_PU8_FAULTCODE
    M_PU9_FAULTCODE = realdata[37]
    data['PU9_FAULTCODE'] = M_PU9_FAULTCODE
    M_UW1_AMP = realdata[38]
    data['UW1_AMP'] = M_UW1_AMP
    M_UW2_AMP = realdata[39]
    data['UW2_AMP'] = M_UW2_AMP
    M_RW1_AMP = realdata[40]
    data['RW1_AMP'] = M_RW1_AMP
    M_RW2_AMP = realdata[41]
    data['RW2_AMP'] = M_RW2_AMP
    M_INFEED_AMP = realdata[42]
    data['INFEED_AMP'] = M_INFEED_AMP
    M_OUTFEED_AMP = realdata[43]
    data['OUTFEED_AMP'] = M_OUTFEED_AMP
    M_PU1_AMP = realdata[44]
    data['PU1_AMP'] = M_PU1_AMP
    M_PU2_AMP = realdata[45]
    data['PU2_AMP'] = M_PU2_AMP
    M_PU3_AMP = realdata[46]
    data['PU3_AMP'] = M_PU3_AMP
    M_PU4_AMP = realdata[47]
    data['PU4_AMP'] = M_PU4_AMP
    M_PU5_AMP = realdata[48]
    data['PU5_AMP'] = M_PU5_AMP
    M_PU6_AMP = realdata[49]
    data['PU6_AMP'] = M_PU6_AMP
    M_PU7_AMP = realdata[50]
    data['PU7_AMP'] = M_PU7_AMP
    M_PU8_AMP = realdata[51]
    data['PU8_AMP'] = M_PU8_AMP
    M_PU9_AMP = realdata[52]
    data['PU9_AMP'] = M_PU9_AMP
    M_UW1_MOTOR_TEMP = realdata[53]
    data['UW1_MOTOR_TEMP'] = M_UW1_MOTOR_TEMP
    M_UW2_MOTOR_TEMP = realdata[54]
    data['UW2_MOTOR_TEMP'] = M_UW2_MOTOR_TEMP
    M_RW1_MOTOR_TEMP = realdata[55]
    data['RW1_MOTOR_TEMP'] = M_RW1_MOTOR_TEMP
    M_RW2_MOTOR_TEMP = realdata[56]
    data['RW2_MOTOR_TEMP'] = M_RW2_MOTOR_TEMP
    M_INFEED_MOTOR_TEMP = realdata[57]
    data['INFEED_MOTOR_TEMP'] = M_INFEED_MOTOR_TEMP
    M_OUTFEED_MOTOR_TEMP = realdata[58]
    data['OUTFEED_MOTOR_TEMP'] = M_OUTFEED_MOTOR_TEMP
    M_PU1_MOTOR_TEMP = realdata[59]
    data['PU1_MOTOR_TEMP'] = M_PU1_MOTOR_TEMP
    M_PU2_MOTOR_TEMP = realdata[60]
    data['PU2_MOTOR_TEMP'] = M_PU2_MOTOR_TEMP
    M_PU3_MOTOR_TEMP = realdata[61]
    data['PU3_MOTOR_TEMP'] = M_PU3_MOTOR_TEMP
    M_PU4_MOTOR_TEMP = realdata[62]
    data['PU4_MOTOR_TEMP'] = M_PU4_MOTOR_TEMP
    M_PU5_MOTOR_TEMP = realdata[63]
    data['PU5_MOTOR_TEMP'] = M_PU5_MOTOR_TEMP
    M_PU6_MOTOR_TEMP = realdata[64]
    data['PU6_MOTOR_TEMP'] = M_PU6_MOTOR_TEMP
    M_PU7_MOTOR_TEMP = realdata[65]
    data['PU7_MOTOR_TEMP'] = M_PU7_MOTOR_TEMP
    M_PU8_MOTOR_TEMP = realdata[66]
    data['PU8_MOTOR_TEMP'] = M_PU8_MOTOR_TEMP
    M_PU9_MOTOR_TEMP =realdata[67]
    data['PU9_MOTOR_TEMP'] = M_PU9_MOTOR_TEMP
    M_WEB_WIDTH = realdata[68]
    data['WEB_WIDTH'] = M_WEB_WIDTH
    M_WEB_THICKNESS = realdata[69]
    data['WEB_THICKNESS'] = M_WEB_THICKNESS
    M_TOTAL_MACHINE_TIME = realdata[70]
    data['TOTAL_MACHINE_TIME'] = M_TOTAL_MACHINE_TIME
    M_TOTAL_MACHINE_RUN_TIME = realdata[71]
    data['TOTAL_MACHINE_RUN_TIME'] = M_TOTAL_MACHINE_RUN_TIME
    M_PU1_SELECT = realdata[72]
    data['PU1_SELECT'] = M_PU1_SELECT
    M_PU2_SELECT = realdata[73]
    data['PU2_SELECT'] = M_PU2_SELECT
    M_PU3_SELECT = realdata[74]
    data['PU3_SELECT'] = M_PU3_SELECT
    M_PU4_SELECT = realdata[75]
    data['PU4_SELECT'] = M_PU4_SELECT
    M_PU5_SELECT = realdata[76]
    data['PU5_SELECT'] = M_PU5_SELECT
    M_PU6_SELECT = realdata[77]
    data['PU6_SELECT'] = M_PU6_SELECT
    M_PU7_SELECT = realdata[78]
    data['PU7_SELECT'] = M_PU7_SELECT
    M_PU8_SELECT = realdata[79]
    data['PU8_SELECT'] = M_PU8_SELECT
    M_PU9_SELECT = realdata[80]
    data['PU9_SELECT'] = M_PU9_SELECT
    M_MACHINE_MANUAL_MODE = realdata[81]
    data['MACHINE_MANUAL_MODE'] = M_MACHINE_MANUAL_MODE
    M_MACHINE_AUTO_MODE = realdata[82]
    data['MACHINE_AUTO_MODE'] = M_MACHINE_AUTO_MODE
    M_MACHINE_STANDBY = realdata[83]
    data['MACHINE_STANDBY'] = M_MACHINE_STANDBY
    M_MACHINE_ERROR_MODE = realdata[84]
    data['MACHINE_ERROR_MODE'] = M_MACHINE_ERROR_MODE
    M_MACHINE_ESTOP = realdata[85]
    data['MACHINE_ESTOP'] = M_MACHINE_ESTOP
    M_ACTUAL_SPEED = realdata[86]
    data['ACTUAL_SPEED'] = M_ACTUAL_SPEED
    return JsonResponse(data)

def KohliELS(request):
    return render(request,'kohli_els/KohliELS_1.html')


def trials(request):
    return render(request,'kohli_els/trial.html')


