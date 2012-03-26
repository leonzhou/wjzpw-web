from StringIO import StringIO
import datetime
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.template.context import RequestContext
from random import choice
import Image
import ImageDraw
from wjzpw import settings
from wjzpw.web.controllers.utils import Utils
from wjzpw.web.forms import LoginForm, FeedbackForm
from wjzpw.web.models import City, Captcha, Announcement, FriendlyLink
from django.utils import simplejson

dashboard_page = "../views/dashboard.html"
feedback_page = "../views/feedback.html"

def dashboard(request):
    """ Renders Dashboard/Home page. """
    login_form = LoginForm()
    announce_list = Announcement.objects.filter(end_date__gte=datetime.datetime.today()).order_by('-updated_at')
    link_list = FriendlyLink.objects.filter(is_active=True).order_by('updated_at')
    return render_to_response(
        dashboard_page, {}, RequestContext(request, {
            'login_form':login_form,
            'announce_list':announce_list,
            'link_list':link_list
        }),
    )

def login(request):
    """ Renders Dashboard/Home page. """
    login_form = LoginForm(request.POST)
    return render_to_response(
        dashboard_page, {}, RequestContext(request, {
            'login_form':login_form,
            }),
    )

def feedback(request):
    """ Renders Feedback page. """
    if request.method == 'GET':
        feedback_from = FeedbackForm()
        success = False
    else:
        feedback_from = FeedbackForm(request.POST)
        success = True

    return render_to_response(
        feedback_page, {}, RequestContext(request, {
            'feedback_from':feedback_from,
            'success':success
            }),
    )

def ajax_get_city_by_province(request, province_id):
    """
    Get city list by province ID
    """
    data = ''
    if request.method == 'GET':
        city_list = City.objects.filter(province = int(province_id))
        data = simplejson.dumps(Utils.generate_options(city_list))
    return HttpResponse(data, 'application/json')

def verify_image(request):
    """
    Get verify code
    """
    captcha_text = Captcha(request).get()
    response = HttpResponse()
    if captcha_text:
        image = Image.new("RGBA", (settings.LENGTH * settings.FONT_SIZE - 26, settings.FONT_SIZE), (0,0,0,0))
        canvas = ImageDraw.Draw(image)

        for i in range(0, len(captcha_text)):
            # font = ImageFont.truetype(choice(captcha.FONTS), captcha.FONT_SIZE)
            # canvas.text((captcha.FONT_SIZE*i+2, -4), captcha_text[i], font = font, fill = choice(captcha.COLOURS))
            horizon = 1; verticality  = -1
            if i>0: horizon = (settings.FONT_SIZE - 5) * i
            if i%2 == 0: verticality = 2
            canvas.text((horizon, verticality), captcha_text[i], fill = choice(settings.COLOURS))

        out = StringIO()
        image.save(out, "PNG")
        out.seek(0)
        response['Content-Type'] = 'image/png'
        response.write(out.read())

    return response