from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from .views import AdminCreateUserApiView


@receiver(AdminCreateUserApiView.user_signal, sender='send_user_mail')
def send_user_mail(sender, user_data, *args, **kwargs):
    template_name = 'user/user_admin_create_mail.html'
    subject = 'Oneum Hello'
    context = {'password': user_data.get('password')}
    html_content = render_to_string(template_name=template_name, context=context)

    message = EmailMultiAlternatives(subject=subject, to=[user_data.get('email'), ])
    message.attach_alternative(content=html_content, mimetype='text/html')
    message.send()
