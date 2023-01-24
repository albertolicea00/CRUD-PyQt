from view.Search__show_teachers_per_teaching_category import *


class Search__show_teachers_per_teaching_categoryController():
    def __init__(self, repo, repoService):
        self.__repository = repo
        self.__repositoryService = repoService

    def run(self):
        try:
            self.__view = Search__show_teachers_per_teaching_category(self)
            self.assigOption()
            self.__validateOpen()
            self.__view.show()
        except Exception as e:
            self.__view.showError(e.args[0])

    def search(self):
        try:
            teaching_category = self.__view.value_teaching_category
            found = self.__repositoryService.show_teachers_per_teaching_category(teaching_category)
            msg = None
            if teaching_category != "":
                if len(found) == 0:
                    msg = f"We dont have any {teaching_category} teacher who have left abroad in the repository"
                elif len(found) == 1:
                    msg = f"This is the only {teaching_category} teacher who have left abroad\n"
                elif len(found) > 1:
                    msg = f"They are the {teaching_category}s teachers who have left abroad\n"
            else:
                raise Exception("Please insert a teacher before make any Operation")

            for i in range(len(found)):
                tch = found[i]
                tch_msg = f"   - {tch.ID}, {tch.fullname.name} {tch.fullname.last_name}\n"
                msg += tch_msg

            self.__view.showResult(msg)
        except Exception as e:
            self.__view.showError(e.args[0])

    # ------------------------------------------------------
    #			Load Options
    # ------------------------------------------------------
    def assigOption(self):
        if self.__view.box_teaching_category.count() != 0:
            self.__view.box_teaching_category.clear()

        for i in self.__repository.getTeacher(att="teachingcategory"):
            teaching_category_tch = i[0]
            teaching_category_box = []

            for j in range(self.__view.box_teaching_category.count() + 1):
                teaching_category_box.append(self.__view.box_teaching_category.itemText(j))

            if teaching_category_tch not in teaching_category_box:
                self.__view.box_teaching_category.addItem(str(teaching_category_tch))

    # ------------------------------------------------------
    #			VALIDATIONS
    # ------------------------------------------------------
    def __validateOpen(self):
        if self.__view.box_teaching_category.count() == 0:
            raise Exception("You must input at least one Teacher before make any seacrh")
