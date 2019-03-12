from selene.conditions import visible, exist, clickable

from testlib import actions
from testlib.matchers import check_that
from testlib.menus import edit_menu, effects_menu


class Editor:

    @staticmethod
    def check_finish_button_visible(prestep=None, timeout=None, repeat=None):
        check_that(edit_menu.finish_edit_button.should, visible, 'Finish button is displayed', prestep=prestep,
                   timeout=timeout, repeat=repeat)

    @staticmethod
    def check_finish_button_not_exist(prestep=None, timeout=None, repeat=None):
        check_that(edit_menu.finish_edit_button.should_not, exist, 'Finish button is not exist', prestep=prestep,
                   timeout=timeout, repeat=repeat)

    @staticmethod
    def check_back_button_clickable(prestep=None, timeout=None, repeat=None):
        check_that(edit_menu.editor_menu_back_button.should, clickable,
                   'Editor menu back button is displayed and active', prestep=prestep, timeout=timeout, repeat=repeat)


class Effects:

    @staticmethod
    def check_none_button_clickable():
        check_that(
            actions.search_element_via_scroll(effects_menu.none_button, scroll_from_el=effects_menu.menu_options[-2],
                                              scroll_to_el=effects_menu.editor_menu_back_button).should, clickable,
            'NONE icon is displayed and active')

    @staticmethod
    def check_glow_button_clickable():
        check_that(
            actions.search_element_via_scroll(effects_menu.glow_button, scroll_from_el=effects_menu.menu_options[-2],
                                              scroll_to_el=effects_menu.editor_menu_back_button).should, clickable,
            'GLOW icon is displayed and active')

    @staticmethod
    def check_poster_button_clickable():
        check_that(
            actions.search_element_via_scroll(effects_menu.poster_button, scroll_from_el=effects_menu.menu_options[-2],
                                              scroll_to_el=effects_menu.editor_menu_back_button).should, clickable,
            'POSTER icon is displayed and active')

    @staticmethod
    def check_pixelate_button_clickable():
        check_that(
            actions.search_element_via_scroll(effects_menu.pixelate_button,
                                              scroll_from_el=effects_menu.menu_options[-2],
                                              scroll_to_el=effects_menu.editor_menu_back_button).should, clickable,
            'PIXELATE icon is displayed and active')

    @staticmethod
    def check_pointillize_button_clickable():
        check_that(actions.search_element_via_scroll(effects_menu.pointillize_button,
                                                     scroll_from_el=effects_menu.menu_options[-2],
                                                     scroll_to_el=effects_menu.editor_menu_back_button).should,
                   clickable, 'POINTILLIZE icon is displayed and active')

    @staticmethod
    def check_edges_button_clickable():
        check_that(
            actions.search_element_via_scroll(effects_menu.edges_button, scroll_from_el=effects_menu.menu_options[-2],
                                              scroll_to_el=effects_menu.editor_menu_back_button).should, clickable,
            'EDGES icon is displayed and active')

    @staticmethod
    def check_lineart_button_clickable():
        check_that(
            actions.search_element_via_scroll(effects_menu.lineart_button, scroll_from_el=effects_menu.menu_options[-2],
                                              scroll_to_el=effects_menu.editor_menu_back_button).should, clickable,
            'LINEART icon is displayed and active')
