from django.forms import ModelForm
from books.models import FavouriteBook

def string_list_to_string(string):
      return string.replace("[", "").replace("]", "").replace("\"", "").replace("'", "")

class FavouriteBookForm(ModelForm):
      class Meta:
         model = FavouriteBook
         fields = "__all__"
         
      def clean(self):
            cleaned_data = super(FavouriteBookForm, self).clean()
            cleaned_data["key"] = string_list_to_string(cleaned_data["key"]).split("/")[-1]
            cleaned_data["title"] = string_list_to_string(cleaned_data["title"])
            cleaned_data["author_name"] = string_list_to_string(cleaned_data["author_name"])
            cleaned_data["image"] = string_list_to_string(cleaned_data["image"])
            return cleaned_data