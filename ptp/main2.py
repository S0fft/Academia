import matplotlib.pyplot as plt
import networkx as nx


class ScheduleSystem:
    def __init__(self):
        self.schedule = nx.DiGraph()

    def add_course(self, course_name, prerequisites=None):
        if prerequisites:
            for prerequisite in prerequisites:
                self.schedule.add_edge(prerequisite, course_name)
        else:
            self.schedule.add_node(course_name)

    def generate_schedule(self):
        schedule = list(nx.topological_sort(self.schedule))
        return schedule


if __name__ == "__main__":
    schedule_system = ScheduleSystem()

    schedule_system.add_course("Аналіз даних та знань")
    schedule_system.add_course("WEB-технології та WEB-дізайн-2", prerequisites=["Аналіз даних та знань"])
    schedule_system.add_course("Теорія інформації", prerequisites=["Аналіз даних та знань"])
    schedule_system.add_course("Іноземна мова", prerequisites=["Теорія інформації", "Аналіз даних та знань"])
    schedule_system.add_course("Основи охорони праці", prerequisites=["Тайм-менеджмент", "Теорія інформації"])

    schedule = schedule_system.generate_schedule()
    print("Розклад занять:")
    for index, course in enumerate(schedule, start=1):
        print(f"{index}. {course}")

    nx.draw(schedule_system.schedule, with_labels=True, font_weight='bold')
    plt.show()
