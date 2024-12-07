from django.dispatch import receiver
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .models import Order


@receiver(post_save, sender=Order)
def email_sender(sender, instance: Order, created, **kwargs):
    if not created:
        return

    template_name = 'order/order_mail.html'
    subject = 'You have new Buyer'
    context = {'phone': instance.phone, 'full_name': instance.full_name, 'key': instance.token_auth}
    html_content = render_to_string(template_name=template_name, context=context)

    message = EmailMultiAlternatives(subject=subject, to=[settings.DEFAULT_FROM_EMAIL, ])
    message.attach_alternative(content=html_content, mimetype='text/html')
    message.send()
