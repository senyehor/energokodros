from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import View

from admin.decorators import admin_rights_required
from admin.logic import _get_message_for_registration_request
from admin.models import UserRegistrationRequest
from users.forms import UserRegistrationRequestsDecisionForm
from users.models import UserRole


@admin_rights_required
def admin_page(request: HttpRequest):
    return render(
        request,
        'admin.html',
        {
            'pending_registration_requests_form': UserRegistrationRequestsDecisionForm()
        }
    )


class RegistrationRequestReview(View):
    http_method_names = ['post']

    def post(self, request: HttpRequest):  # noqa
        if decision := request.POST.get('decision'):  # noqa
            f = request.POST
            try:
                registration_request = UserRegistrationRequest.objects.get(
                    id=f['user_registration_request']
                )
                # todo lower
                if decision.lower() == 'схвалити':
                    UserRole(
                        position=f['position'],
                        access_level_id=f['access_level'],
                        institution=registration_request.institution,
                        user=registration_request.user
                    ).save()
                elif decision.lower() == 'відмовити':
                    registration_request.user.delete()
                else:
                    return HttpResponse(status=400)
                registration_request.delete()
                return redirect('admin_page')
            except KeyError:
                return HttpResponse(status=400)

        return HttpResponse(status=400)


class GetMessageForRegistrationRequest(View):
    http_method_names = ['post']

    # @method_decorator(admin) todo
    def post(self, request: HttpRequest):  # noqa
        if request.is_ajax():  # noqa
            if request_id := request.POST.get('request_id'):  # noqa
                return JsonResponse(
                    {'message': _get_message_for_registration_request(request_id)},
                    status=200
                )
        return HttpResponse(status=405)
