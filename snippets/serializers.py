from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # Serializer和Django中Form功能相似
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
