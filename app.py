from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.popup import Popup
from datetime import date, datetime
import csv_cleared
from kivy.core.window import Window



###################Menus du jour, développé par Enzo###################
class Lundi(Screen):
    entree_lundi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 0, 1, 0))
    plat_lundi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 1, 2, 0))
    laitier_lundi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 2, 3, 0))
    dessert_lundi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 3, 4, 0))


class Mardi(Screen):
    entree_mardi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 0, 1, 1))
    plat_mardi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 1, 2, 1))
    laitier_mardi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 2, 3, 1))
    dessert_mardi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 3, 4, 1))


class Mercredi(Screen):
    entree_mercredi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 0, 1, 2))
    plat_mercredi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 1, 2, 2))
    laitier_mercredi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 2, 3, 2))
    dessert_mercredi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 3, 4, 2))


class Jeudi(Screen):
    entree_jeudi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 0, 1, 3))
    plat_jeudi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 1, 2, 3))
    laitier_jeudi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 2, 3, 3))
    dessert_jeudi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 3, 4, 3))


class Vendredi(Screen):
    entree_vendredi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 0, 1, 4))
    plat_vendredi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 1, 2, 4))
    laitier_vendredi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 2, 3, 4))
    dessert_vendredi = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 3, 4, 4))

###################Menus du soir, développé par Enzo###################


class LundiSoir(Screen):
    entree_lundi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 0, 1, 5))
    plat_lundi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 1, 2, 5))
    laitier_lundi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 2, 3, 5))
    dessert_lundi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 3, 4, 5))


class MardiSoir(Screen):
    entree_mardi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 0, 1, 6))
    plat_mardi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 1, 2, 6))
    laitier_mardi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 2, 3, 6))
    dessert_mardi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 3, 4, 6))


class MercrediSoir(Screen):
    entree_mercredi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 0, 1, 7))
    plat_mercredi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 1, 2, 7))
    laitier_mercredi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 2, 3, 7))
    dessert_mercredi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 3, 4, 7))


class JeudiSoir(Screen):
    entree_jeudi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 0, 1, 8))
    plat_jeudi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 1, 2, 8))
    laitier_jeudi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 2, 3, 8))
    dessert_jeudi_soir = ',\n \n'.join(
        csv_cleared.plat_jour(csv_cleared.menu, 3, 4, 8))

###################


class MyApp(App):
    """Classe principale structurant l'application"""  # Classe entièrement développée par Enzo

    def build(self):
        """Construction de l'animation"""
        self.root = WindowManager()
        self.menu_of_day()
        return self.root

    def menu_of_day(self):
        """Affichage d'un menu en fonction du jour de la semaine et de l'heure"""
        jour = date.today().weekday()
        heure = datetime.now().hour
        if jour == 0:
            self.root.current = 'lundi'
            if heure >= 17:
                self.root.current = 'lundi_soir'
        elif jour == 1:
            self.root.current = 'mardi'
            if heure >= 17:
                self.root.current = 'mardi_soir'
        elif jour == 2:
            self.root.current = 'mercredi'
            if heure >= 17:
                self.root.current = 'mercredi_soir'
        elif jour == 3:
            self.root.current = 'jeudi'
            if heure >= 17:
                self.root.current = 'jeudi_soir'
        elif jour == 4:
            self.root.current = 'vendredi'
        return self.root.current

    def bio(self, menu):
        """Détermine s'il s'agit d'un met bio"""
        if menu.count("*") == 1:  # S'il y a un "*", alors c'est un met bio et on retourne True
            return True
        else:
            return False

###################


class CreditPopup(FloatLayout):
    """Fenêtre de crédits"""  # Dévoloppé par Enzo
    pass


class HelpPopup(FloatLayout):
    """Fenêtre d'aide"""  # Développé par Elouann
    pass

###################


class Background(Widget):
    """Fond d'écran"""  # Classe dévoloppée par Enzo
    bg_color = ListProperty([1, 1, 1])
    ban_color = ListProperty([.082, .631, .192])
    txt_color = ListProperty([0, 0, 0, 1])

###################


class WindowManager(ScreenManager):
    """Gère les écrans et les fonctions"""  # Classe dévoloppée par Enzo
    MY_GLOBAL = NumericProperty(
        0)  # Pour que le mode sombre s'applique sur tous les écrans

    def animate_button(self, widget, *args):
        """"Anime la bannière latérale gauche"""
        anim = Animation(
            right_hint=.3, duration=0.3)  # Réalise une animation de 0.3 secondes d'un rectangle
        # d'un pourcentage de l'écran de 0.3
        anim.bind(on_progress=self.progress_callback)
        anim.start(widget)

    def deanimate_button(self, widget, *args):
        """Fait disparaître la bannière latéral gauche"""
        anim = Animation(
            right_hint=-.3, duration=0.3)  # Fait disparaître le rectangle
        anim.bind(on_progress=self.progress_callback)
        anim.start(widget)

    def progress_callback(self, *args):
        """Permet d'effectuer un callback pour l'animation"""
        progress = args[2]

    def night(self, widget, *args):
        """Mode sombre"""
        nuit = Animation(bg_color=(0.113, 0.125, 0.133, 1),
                         ban_color=(0, 0, 0, 1), txt_color=(1, 1, 1, 1))
        nuit.start(widget)

    def day(self, widget, *args):
        """Mode clair, par défaut"""
        jour = Animation(bg_color=(1, 1, 1, 1),
                         ban_color=(.082, .631, .192, 1), txt_color=(0, 0, 0, 1))
        jour.start(widget)

    def credit_popup(self, *args):
        """Popup des crédits"""
        show = CreditPopup()
        popupWindow = Popup(title="Crédits", content=show,
                            size_hint=(None, None), size=(Window.width/1.5, Window.height/1.5))
        popupWindow.open()

    def help_popup(self, *args):
        """Popup d'aide"""
        # Développé par Elouann
        show = HelpPopup()
        popupWindow = Popup(title="Aide", content=show,
                            size_hint=(None, None), size=(Window.width/1.5, Window.height/1.5))
        popupWindow.open()


if __name__ == '__main__':
    MyApp().run()
