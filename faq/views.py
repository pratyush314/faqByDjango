from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.utils.translation import get_language
from django.core.cache import cache

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return cached_data

        queryset = super().get_queryset()
        for faq in queryset:
            faq.question = faq.get_translated_question(lang)
            faq.answer = faq.get_translated_answer(lang)
        cache.set(cache_key, queryset, timeout=60 * 15)
        return queryset
