import matplotlib.pyplot as plt
import networkx as nx


class Course:
    def __init__(self, name, teacher, room, students):
        self.name = name
        self.teacher = teacher
        self.room = room
        self.students = students


def create_conflict_graph(courses):
    G = nx.Graph()
    for i, course1 in enumerate(courses):
        for j, course2 in enumerate(courses):
            if i >= j:
                continue
            if course1.teacher == course2.teacher or \
               course1.room == course2.room or \
               not set(course1.students).isdisjoint(course2.students):
                G.add_edge(course1.name, course2.name)
    return G


def color_schedule(graph):
    return nx.coloring.greedy_color(graph, strategy='largest_first')


if __name__ == "__main__":
    courses = [
        Course("Аналіз даних та знань", "Гудкова К.Ю.", "Room 2428", {"", ""}),
        Course("WEB-технології-2", "Нечволода Л.В.", "Room 2428", {"", ""}),
        Course("Теорія інформації", "Беш А.М.", "Room 2428", {"", ""}),
        Course("Іноземна мова", "Ковальова Н.І.", "Room 2428", {""}),
        Course("Випадкові процеси", "Гітіс В.Б.", "Room 2428", {"", ""}),
        Course("Проектно-технологічна практика", "Гудкова К.Ю.", "Room 2428", {"", ""}),
    ]

    conflict_graph = create_conflict_graph(courses)

    schedule = color_schedule(conflict_graph)

    for course, timeslot in schedule.items():
        print(f"Course: {course}, Timeslot: {timeslot}")

    pos = nx.spring_layout(conflict_graph)
    nx.draw(conflict_graph, pos, with_labels=True, node_color=list(schedule.values()), cmap=plt.cm.tab20)
    plt.show()
