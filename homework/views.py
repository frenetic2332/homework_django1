from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        return {
            "header": "home"
        }

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        return {
            "header": "about"
        }

class ContactsView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        return {
            "header": "contacts"
        }