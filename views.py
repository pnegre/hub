# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import simplejson
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

from hub.models import *


@login_required
def index(request):
    return render_to_response(
            'hub/index.html', {
    }, context_instance=RequestContext(request))


@login_required
def menu(request):
    menus = Menu.objects.all()
    menus_to_render = []

    if len(menus) > 0:
        for m in menus.order_by('pos'):
            r = []
            subs = SubMenu.objects.filter(menu=m)
            if len(subs) > 0:
                for s in subs.order_by('pos'):
                    if s.superuser_only:
                        if request.user.is_superuser:
                            r.append(s)
                        continue

                    perms = s.permissions.all()
                    if len(perms) == 0:
                        r.append(s)
                        continue

                    for p in perms:
                        p = p.content_type.app_label + '.' + p.codename
                        if request.user.has_perm(p):
                            r.append(s)
                            break

                if len(r) > 0:
                    menus_to_render.append({'menu': m, 'subs': r})
    else:
        menus_to_render = [{ 'menu': { 'name': "No s'han definit menus"}, 'subs': [] }]

    return render_to_response(
        'hub/menu.html', {
            'menus': menus_to_render,
    }, context_instance=RequestContext(request))
