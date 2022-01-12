from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Components.utility import CustomHLayout, CustomLabel, CustomSizePolicy, CustomVLayout


class UserTab(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(855, 590)
        self.userTab_layout = CustomVLayout(self, spacing=0)

        self.UserScrollArea = QScrollArea(self)
        self.UserScrollArea.setWidgetResizable(True)
        self.scrollarea_widget = QWidget()
        self.scrollarea_widget.setGeometry(QRect(0, 0, 853, 588))
        self.scrollarea_layout = CustomVLayout(self.scrollarea_widget)

        self.panel_0 = QFrame(self.scrollarea_widget)
        self.panel_0.setMinimumSize(QSize(0, 50))
        self.panel_0.setMaximumSize(QSize(16777215, 50))
        self.scrollarea_layout.addWidget(self.panel_0)

        self.panel0_layout = CustomHLayout(self.panel_0, (20, -1, 20, -1), 15)

        self.player_icon = CustomLabel(self.panel_0, minSize=(30, 0), maxSize=(30, 16777215), image="Assets/Placeholders/user_info_icon.png")
        self.panel0_layout.addWidget(self.player_icon)


        self.player_info_title = CustomLabel(self.panel_0, text="player info", font_size=14, font_style="SemiBold")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.player_info_title)
        self.panel0_layout.addWidget(self.player_info_title)

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.panel0_layout.addItem(spacerItem)

        self.std_label = CustomLabel(self.panel_0, text="osu!", font_style="Bold", font_size=10)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.std_label)
        self.panel0_layout.addWidget(self.std_label)


        self.taiko_label = CustomLabel(self.panel_0, text="osu!taiko", font_style="SemiBold", font_size=9, color="rgb(255, 102, 171)")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.taiko_label)
        self.panel0_layout.addWidget(self.taiko_label)

		
        self.catch_label = CustomLabel(self.panel_0, text="osu!catch", font_style="SemiBold", font_size=9, color="rgb(255, 102, 171)")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.catch_label)
        self.panel0_layout.addWidget(self.catch_label)


        self.mania_label = CustomLabel(self.panel_0, text="osu!mania", font_style="SemiBold", font_size=9, color="rgb(255, 102, 171)")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.mania_label)
        self.panel0_layout.addWidget(self.mania_label)


        self.panel_1 = QFrame(self.scrollarea_widget)
        sizePolicy = CustomSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed, self.panel_1)
        self.panel_1.setMaximumSize(QSize(16777215, 200))

        self.panel1_layout = CustomHLayout(self.panel_1, (20, -1, 20, -1))

        self.section1 = QFrame(self.panel_1)
        self.section1.setMinimumSize(QSize(0, 128))
        self.section1.setMaximumSize(QSize(16777215, 128))

        self.section1_layout = CustomHLayout(self.section1, (0, -1, -1, -1), 9)

        self.profile_picture = CustomLabel(self.section1, image="Assets/Placeholders/avatar-guest.png", minSize=(128, 100), maxSize=(128, 128))
        sizePolicy = CustomSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred, self.profile_picture)
        self.section1_layout.addWidget(self.profile_picture)


        self.username_label = CustomLabel(self.section1, text="JohnDoe")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.username_label)
        self.username_label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.section1_layout.addWidget(self.username_label)

        self.panel1_layout.addWidget(self.section1)


        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.panel1_layout.addItem(spacerItem1)
		
        self.section2 = QFrame(self.panel_1)
        self.section2.setMinimumSize(QSize(222, 148))
        self.section2.setMaximumSize(QSize(222, 148))
        self.section2_layout = CustomHLayout(self.section2)

        self.labels_frame = QFrame(self.section2)
        self.label_frame_layout = CustomVLayout(self.labels_frame)

        self.ranked_score_label = CustomLabel(self.labels_frame, "Ranked Score")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.ranked_score_label)
        self.ranked_score_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.label_frame_layout.addWidget(self.ranked_score_label)

        self.hit_accuracy_label = CustomLabel(self.labels_frame, "Hit Accuracy")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.hit_accuracy_label)
        self.label_frame_layout.addWidget(self.hit_accuracy_label)

        self.playcount_label = CustomLabel(self.labels_frame, "Play Count")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.playcount_label)

        self.label_frame_layout.addWidget(self.playcount_label)

        self.total_score_label = CustomLabel(self.labels_frame, "Total Score")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.total_score_label)
        self.label_frame_layout.addWidget(self.total_score_label)

        self.total_hits_label = CustomLabel(self.labels_frame, "Total Hits")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.total_hits_label)
        self.label_frame_layout.addWidget(self.total_hits_label)

        self.max_combo_label = CustomLabel(self.labels_frame, "Maximum Combo")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.max_combo_label)
        self.label_frame_layout.addWidget(self.max_combo_label)

        self.section2_layout.addWidget(self.labels_frame)

        self.fields_frame = QFrame(self.section2)
        self.fields_frame.setLayoutDirection(Qt.RightToLeft)
        self.userTab_layout_18 = CustomVLayout(self.fields_frame)

        self.ranked_score_value = CustomLabel(self.fields_frame, "314,722,286")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.ranked_score_value)
        self.userTab_layout_18.addWidget(self.ranked_score_value)

        self.hit_accuracy_value = CustomLabel(self.fields_frame, "97.18%")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.hit_accuracy_value)
        self.userTab_layout_18.addWidget(self.hit_accuracy_value)

        self.playcount_value = CustomLabel(self.fields_frame, "2,595")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.playcount_value)
        self.userTab_layout_18.addWidget(self.playcount_value)

        self.total_score_value = CustomLabel(self.fields_frame, "948,856,855")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.total_score_value)
        self.userTab_layout_18.addWidget(self.total_score_value)

        self.total_hits_value = CustomLabel(self.fields_frame, "324,552")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.total_hits_value)
        self.userTab_layout_18.addWidget(self.total_hits_value)

        self.max_combo_value = CustomLabel(self.fields_frame, "1,027")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.max_combo_value)
        self.userTab_layout_18.addWidget(self.max_combo_value)

        self.section2_layout.addWidget(self.fields_frame)

        self.panel1_layout.addWidget(self.section2)

        self.scrollarea_layout.addWidget(self.panel_1)

        self.panel_2 = QFrame(self.scrollarea_widget)
        self.panel_2.setMinimumSize(QSize(0, 65))
        self.panel_2.setMaximumSize(QSize(16777215, 65))

        self.panel1_layout_3 = CustomHLayout(self.panel_2, (20, -1, 20, -1), 15)

        self.total_play_time_frame = QFrame(self.panel_2)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.total_play_time_frame)
        self.userTab_layout_3 = CustomVLayout(self.total_play_time_frame)
        self.total_play_time_label = CustomLabel(self.total_play_time_frame, "Total Play Time", font_size=9, font_style="Bold")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.total_play_time_label)
        self.userTab_layout_3.addWidget(self.total_play_time_label)

        self.total_play_time_value = CustomLabel(self.total_play_time_frame, "4d 21h 31m")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.total_play_time_value)
        self.userTab_layout_3.addWidget(self.total_play_time_value)

        self.panel1_layout_3.addWidget(self.total_play_time_frame)

        self.medal_count_frame = QFrame(self.panel_2)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.medal_count_frame)
        self.userTab_layout_4 = CustomVLayout(self.medal_count_frame)
        self.medal_count_label = CustomLabel(self.medal_count_frame, "Medals")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.medal_count_label)
        self.userTab_layout_4.addWidget(self.medal_count_label)

        self.medal_count_value = CustomLabel(self.medal_count_frame, "19")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.medal_count_value)
        self.userTab_layout_4.addWidget(self.medal_count_value)

        self.panel1_layout_3.addWidget(self.medal_count_frame)

        self.weighted_pp_frame = QFrame(self.panel_2)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.weighted_pp_frame)
        self.userTab_layout_5 = CustomVLayout(self.weighted_pp_frame)
        self.weighted_pp_label = CustomLabel(self.weighted_pp_frame, "pp (Weighted)")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.weighted_pp_label)
        self.userTab_layout_5.addWidget(self.weighted_pp_label)

        self.weighted_pp_value = CustomLabel(self.weighted_pp_frame, "700")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.weighted_pp_value)
        self.userTab_layout_5.addWidget(self.weighted_pp_value)

        self.panel1_layout_3.addWidget(self.weighted_pp_frame)

        self.total_pp_frame = QFrame(self.panel_2)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.total_pp_frame)
        self.userTab_layout_6 = CustomVLayout(self.total_pp_frame)
        self.total_pp_label = CustomLabel(self.total_pp_frame, "pp (Total)")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.total_pp_label)
        self.userTab_layout_6.addWidget(self.total_pp_label)

        self.total_pp_value = CustomLabel(self.total_pp_frame, "1220")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.total_pp_value)
        self.userTab_layout_6.addWidget(self.total_pp_value)

        self.panel1_layout_3.addWidget(self.total_pp_frame)

        spacerItem2 = QSpacerItem(239472983, 384729837, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.panel1_layout_3.addItem(spacerItem2)
        
        self.level_frame = QFrame(self.panel_2)
        self.panel1_layout_3.addWidget(self.level_frame)
        self.scrollarea_layout.addWidget(self.panel_2)

        self.panel1_layout_4 = CustomHLayout(self.level_frame, spacing=18)
        self.level_progress = QProgressBar(self.level_frame)
        self.level_progress.setMinimumSize(QSize(230, 0))
        self.level_progress.setMaximumSize(QSize(230, 6))
        self.level_progress.setProperty("value", 24)
        self.level_progress.setTextVisible(False)
        self.level_progress.setFormat("")
        self.panel1_layout_4.addWidget(self.level_progress)

        self.level_value = CustomLabel(self.level_frame, "40", minSize=(43, 43), maxSize=(43, 43))
        self.level_value.setAlignment(Qt.AlignCenter)
        self.panel1_layout_4.addWidget(self.level_value)


        self.panel_3 = QFrame(self.scrollarea_widget)
        self.panel_3.setMaximumSize(QSize(16777215, 300))
        self.panel1_layout_8 = CustomHLayout(self.panel_3)
        self.left_container = QFrame(self.panel_3)
        self.scrollarea_layout3 = CustomVLayout(self.left_container)
        self.mods_frame = QFrame(self.left_container)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.mods_frame)
        self.mods_frame.setLayoutDirection(Qt.LeftToRight)
        self.panel1_layout_10 = CustomHLayout(self.mods_frame)
        self.mod1_box = QFrame(self.mods_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.mod1_box)
        self.mod1_box.setMinimumSize(QSize(35, 45))
        self.mod1_box.setMaximumSize(QSize(40, 45))
        self.userTab_layout_19 = CustomVLayout(self.mod1_box)
        self.mod_1_icon = CustomLabel(self.mod1_box, "0")
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.mod_1_icon)
        self.mod_1_icon.setMinimumSize(QSize(32, 22))
        self.mod_1_icon.setMaximumSize(QSize(32, 22))
        self.mod_1_icon.setPixmap(QtGui.QPixmap(
            ".\\Screens\\../Assets/Mod_Icons/DT.png"))
        self.mod_1_icon.setScaledContents(True)
        self.mod_1_icon.setAlignment(Qt.AlignCenter)
        self.userTab_layout_19.addWidget(self.mod_1_icon)

        self.mod1_value = CustomLabel(self.mod1_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed, self.mod1_value)
        self.mod1_value.setAlignment(Qt.AlignCenter)
        self.userTab_layout_19.addWidget(self.mod1_value)

        self.panel1_layout_10.addWidget(self.mod1_box)

        self.scrollarea_layout3.addWidget(self.mods_frame)

        self.Line_Graph_Frame = QFrame(self.left_container)
        self.scrollarea_layout3.addWidget(self.Line_Graph_Frame)

        self.panel1_layout_8.addWidget(self.left_container)

        self.right_container = QFrame(self.panel_3)
        self.right_container.setMinimumSize(QSize(322, 0))
        self.right_container.setMaximumSize(QSize(322, 16777215))
        self.right_container.setLayoutDirection(Qt.RightToLeft)
        self.userTab_layout_9 = CustomVLayout(self.right_container, (-1, 0, -1, -1))
        self.grade_frame = QFrame(self.right_container)
        self.grade_frame.setLayoutDirection(Qt.LeftToRight)
        self.panel1_layout_6 = CustomHLayout(self.grade_frame, (0, 0, 0, 30))
        self.firsts_box = QFrame(self.grade_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.firsts_box)
        self.firsts_box.setMinimumSize(QSize(45, 45))
        self.firsts_box.setMaximumSize(QSize(45, 45))
        self.userTab_layout_15 = CustomVLayout(self.firsts_box)
        self.icon_1 = CustomLabel(self.firsts_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.icon_1)
        self.icon_1.setMinimumSize(QSize(43, 21))
        self.icon_1.setMaximumSize(QSize(43, 21))
        self.icon_1.setPixmap(QtGui.QPixmap(
            ".\\Screens\\../Assets/Rank_Grades/rank1.png"))
        self.icon_1.setScaledContents(True)
        self.userTab_layout_15.addWidget(self.icon_1)

        self.firsts_value = CustomLabel(self.firsts_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed, self.firsts_value)
        self.firsts_value.setAlignment(Qt.AlignCenter)
        self.userTab_layout_15.addWidget(self.firsts_value)

        self.panel1_layout_6.addWidget(self.firsts_box)

        self.ssh_grade_box = QFrame(self.grade_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.ssh_grade_box)
        self.ssh_grade_box.setMinimumSize(QSize(45, 45))
        self.ssh_grade_box.setMaximumSize(QSize(45, 45))
        self.userTab_layout_14 = CustomVLayout(self.ssh_grade_box)
        self.icon_ssh = CustomLabel(self.ssh_grade_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.icon_ssh)
        self.icon_ssh.setMinimumSize(QSize(43, 21))
        self.icon_ssh.setMaximumSize(QSize(43, 21))
        self.icon_ssh.setPixmap(QtGui.QPixmap(
            ".\\Screens\\../Assets/Rank_Grades/SSH.png"))
        self.icon_ssh.setScaledContents(True)
        self.userTab_layout_14.addWidget(self.icon_ssh)

        self.ssh_grade_value = CustomLabel(self.ssh_grade_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed, self.ssh_grade_value)
        self.ssh_grade_value.setAlignment(Qt.AlignCenter)
        self.userTab_layout_14.addWidget(self.ssh_grade_value)

        self.panel1_layout_6.addWidget(self.ssh_grade_box)

        self.ss_grade_box = QFrame(self.grade_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.ss_grade_box)
        self.ss_grade_box.setMinimumSize(QSize(45, 45))
        self.ss_grade_box.setMaximumSize(QSize(45, 45))
        self.userTab_layout_13 = CustomVLayout(self.ss_grade_box)
        self.icon_ss = CustomLabel(self.ss_grade_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.icon_ss)
        self.icon_ss.setMinimumSize(QSize(43, 21))
        self.icon_ss.setMaximumSize(QSize(43, 21))
        self.icon_ss.setPixmap(QtGui.QPixmap(
            ".\\Screens\\../Assets/Rank_Grades/SS.png"))
        self.icon_ss.setScaledContents(True)
        self.userTab_layout_13.addWidget(self.icon_ss)

        self.ss_grade_value = CustomLabel(self.ss_grade_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed, self.ss_grade_value)
        self.ss_grade_value.setAlignment(Qt.AlignCenter)
        self.userTab_layout_13.addWidget(self.ss_grade_value)

        self.panel1_layout_6.addWidget(self.ss_grade_box)

        self.sh_grade_box = QFrame(self.grade_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.sh_grade_box)
        self.sh_grade_box.setMinimumSize(QSize(45, 45))
        self.sh_grade_box.setMaximumSize(QSize(45, 45))
        self.userTab_layout_12 = CustomVLayout(self.sh_grade_box)
        self.icon_sh = CustomLabel(self.sh_grade_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.icon_sh)
        self.icon_sh.setMinimumSize(QSize(43, 21))
        self.icon_sh.setMaximumSize(QSize(43, 21))
        self.icon_sh.setPixmap(QtGui.QPixmap(
            ".\\Screens\\../Assets/Rank_Grades/SH.png"))
        self.icon_sh.setScaledContents(True)
        self.userTab_layout_12.addWidget(self.icon_sh)

        self.sh_grade_value = CustomLabel(self.sh_grade_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed, self.sh_grade_value)
        self.sh_grade_value.setAlignment(Qt.AlignCenter)
        self.userTab_layout_12.addWidget(self.sh_grade_value)

        self.panel1_layout_6.addWidget(self.sh_grade_box)

        self.s_grade_box = QFrame(self.grade_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.s_grade_box)
        self.s_grade_box.setMinimumSize(QSize(45, 45))
        self.s_grade_box.setMaximumSize(QSize(45, 45))
        self.userTab_layout_11 = CustomVLayout(self.s_grade_box)
        self.icon_s = CustomLabel(self.s_grade_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.icon_s)
        self.icon_s.setMinimumSize(QSize(43, 21))
        self.icon_s.setMaximumSize(QSize(43, 21))
        self.icon_s.setPixmap(QtGui.QPixmap(
            ".\\Screens\\../Assets/Rank_Grades/S.png"))
        self.icon_s.setScaledContents(True)
        self.userTab_layout_11.addWidget(self.icon_s)

        self.s_grade_value = CustomLabel(self.s_grade_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed, self.s_grade_value)
        self.s_grade_value.setStyleSheet(
            "font: 63 10pt \"Torus Pro SemiBold\";")
        self.s_grade_value.setAlignment(Qt.AlignCenter)
        self.userTab_layout_11.addWidget(self.s_grade_value)

        self.panel1_layout_6.addWidget(self.s_grade_box)

        self.a_grade_box = QFrame(self.grade_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.a_grade_box)
        self.a_grade_box.setMinimumSize(QSize(45, 45))
        self.a_grade_box.setMaximumSize(QSize(45, 45))
        self.userTab_layout_10 = CustomVLayout(self.a_grade_box)
        self.icon_a = CustomLabel(self.a_grade_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.icon_a)
        self.icon_a.setMinimumSize(QSize(43, 21))
        self.icon_a.setMaximumSize(QSize(43, 21))
        self.icon_a.setPixmap(QtGui.QPixmap(
            ".\\Screens\\../Assets/Rank_Grades/A.png"))
        self.icon_a.setScaledContents(True)
        self.userTab_layout_10.addWidget(self.icon_a)

        self.a_grade_value = CustomLabel(self.a_grade_box)
        sizePolicy = CustomSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed, self.a_grade_value)
        self.a_grade_value.setStyleSheet(
            "font: 63 10pt \"Torus Pro SemiBold\";")
        self.a_grade_value.setAlignment(Qt.AlignCenter)
        self.userTab_layout_10.addWidget(self.a_grade_value)

        self.panel1_layout_6.addWidget(self.a_grade_box)

        self.userTab_layout_9.addWidget(self.grade_frame)

        self.rank_frame_container = QFrame(self.right_container)
        self.panel1_layout_7 = CustomHLayout(self.rank_frame_container, (0, 0, 0, 50))
        self.rank_frame = QFrame(self.rank_frame_container)
        self.userTab_layout_16 = CustomVLayout(self.rank_frame, spacing=25)
        self.global_ranking_frame = QFrame(self.rank_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.global_ranking_frame)
        self.global_ranking_frame.setLayoutDirection(Qt.LeftToRight)
        self.userTab_layout_7 = CustomVLayout(self.global_ranking_frame, spacing=6)
        self.global_ranking_label = CustomLabel(self.global_ranking_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.global_ranking_label)
        self.global_ranking_label.setLayoutDirection(Qt.LeftToRight)
        self.userTab_layout_7.addWidget(self.global_ranking_label)

        self.global_ranking_value = CustomLabel(self.global_ranking_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.global_ranking_value)
        self.userTab_layout_7.addWidget(self.global_ranking_value)

        self.userTab_layout_16.addWidget(self.global_ranking_frame)

        self.country_ranking_frame = QFrame(self.rank_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred, self.country_ranking_frame)
        self.country_ranking_frame.setLayoutDirection(Qt.LeftToRight)
        self.userTab_layout_8 = CustomVLayout(self.country_ranking_frame, spacing=4)
        self.country_ranking_label = CustomLabel(self.country_ranking_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.country_ranking_label)
        self.userTab_layout_8.addWidget(self.country_ranking_label)

        self.country_ranking_value = CustomLabel(self.country_ranking_frame)
        sizePolicy = CustomSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed, self.country_ranking_value)
        self.userTab_layout_8.addWidget(self.country_ranking_value)

        self.userTab_layout_16.addWidget(self.country_ranking_frame)

        self.panel1_layout_7.addWidget(self.rank_frame)

        spacerItem3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.panel1_layout_7.addItem(spacerItem3)
        self.userTab_layout_9.addWidget(self.rank_frame_container)

        self.panel1_layout_8.addWidget(self.right_container)

        self.scrollarea_layout.addWidget(self.panel_3)

        self.UserScrollArea.setWidget(self.scrollarea_widget)
        self.userTab_layout.addWidget(self.UserScrollArea)


        self.firsts_value.setText("0")
        self.ssh_grade_value.setText("12")
        self.ss_grade_value.setText("54")
        self.sh_grade_value.setText("39")
        self.s_grade_value.setText("80")
        self.a_grade_value.setText("50")
        self.global_ranking_label.setText("Global Ranking")
        self.global_ranking_value.setText("#1,343,987")
        self.country_ranking_label.setText("Country Ranking")
        self.country_ranking_value.setText("#2,000")

        self.setStyleSheet("background:rgb(28, 23, 25);\n"
                           "color: white;")

        self.panel_0.setStyleSheet("background: #2e1f25;")

        self.panel_1.setStyleSheet("background: #2a2226;")

        self.labels_frame.setStyleSheet("font: 63 9pt \"Torus Pro SemiBold\";")

        self.fields_frame.setStyleSheet("font: 75 9pt \"Torus Pro Bold\";")

        self.panel_2.setStyleSheet("background: #382e32")

        self.total_play_time_frame.setStyleSheet("QFrame {\n"
                                                 "border:none;\n"
                                                 "border-top-style:solid;\n"
                                                 "border-width: 2px;\n"
                                                 "border-color: #ff66ab\n"
                                                 "}")


        self.total_play_time_value.setStyleSheet("font: 14pt \"Torus Pro\";border:none;")

        self.medal_count_frame.setStyleSheet("QFrame {\n"
                                             "border:none;\n"
                                             "border-top-style:solid;\n"
                                             "border-width: 2px;\n"
                                             "border-color: #b3d944;\n"
                                             "min-width: 53px;\n"
                                             "}")

        self.medal_count_label.setStyleSheet("border:none;\n"
                                             "font: 75 9pt \"Torus Pro Bold\";")

        self.medal_count_value.setStyleSheet("border: none;\n"
                                             "font: 14pt \"Torus Pro\";")

        self.weighted_pp_frame.setStyleSheet("QFrame {\n"
                                             "border:none;\n"
                                             "border-top-style:solid;\n"
                                             "border-width: 2px;\n"
                                             "border-color: #ed1221\n"
                                             "}")

        self.weighted_pp_label.setStyleSheet("border:none;\n"
                                             "font: 75 9pt \"Torus Pro Bold\";")

        self.weighted_pp_value.setStyleSheet("border: none;\n"
                                             "font: 14pt \"Torus Pro\";")

        self.total_pp_frame.setStyleSheet("QFrame {\n"
                                          "border:none;\n"
                                          "border-top-style:solid;\n"
                                          "border-width: 2px;\n"
                                          "border-color: #ce1c9d\n"
                                          "}")

        self.total_pp_label.setStyleSheet("border:none;\n"
                                          "font: 75 9pt \"Torus Pro Bold\";")

        self.total_pp_value.setStyleSheet("border: none;\n"
                                          "font: 14pt \"Torus Pro\";")

        self.level_progress.setStyleSheet("QProgressBar\n"
                                          "{\n"
                                          "border: solid grey;\n"
                                          "border-radius: 4px;\n"
                                          "background: #1c1719;\n"
                                          "color: #1c1719;\n"
                                          "max-height: 6px;\n"
                                          "}\n"
                                          "QProgressBar::chunk \n"
                                          "{\n"
                                          "background-color: #ff66ab;\n"
                                          "border-radius: 4px;\n"
                                          "border-radius :15px;\n"
                                          "}      ")

        self.level_value.setStyleSheet("font: 15pt \"Torus Pro SemiBold\";\n"
                                       "border-style: solid;\n"
                                       "border-width: 2px;\n"
                                       "border-color: #e6b824;\n"
                                       "border-radius: 15px;\n"
                                       "")

        self.panel_3.setStyleSheet("background: #2a2226;")

        self.mod1_value.setStyleSheet("font: 63 10pt \"Torus Pro SemiBold\";")

        self.username_label.setStyleSheet("font: 20pt \"Torus Pro\";")

        self.firsts_value.setStyleSheet(
            "font: 63 10pt \"Torus Pro SemiBold\";")

        self.ssh_grade_value.setStyleSheet(
            "font: 63 10pt \"Torus Pro SemiBold\";")

        self.ss_grade_value.setStyleSheet(
            "font: 63 10pt \"Torus Pro SemiBold\";")

        self.sh_grade_value.setStyleSheet(
            "font: 63 10pt \"Torus Pro SemiBold\";")

        self.global_ranking_frame.setStyleSheet("QFrame {\n"
                                                "border:none;\n"
                                                "border-top-style:solid;\n"
                                                "border-width: 2px;\n"
                                                "border-color: #ff66ab\n"
                                                "}")

        self.global_ranking_label.setStyleSheet("border:none;\n"
                                                "font: 75 10pt \"Torus Pro Bold\";")

        self.global_ranking_value.setStyleSheet("border: none;\n"
                                                "font: 24pt \"Torus Pro\";")

        self.country_ranking_frame.setStyleSheet("QFrame {\n"
                                                 "border:none;\n"
                                                 "border-top-style:solid;\n"
                                                 "border-width: 2px;\n"
                                                 "border-color: #ff66ab\n"
                                                 "}")

        self.country_ranking_label.setStyleSheet("border:none;\n"
                                                 "font: 75 9pt \"Torus Pro Bold\";")

        self.country_ranking_value.setStyleSheet("border: none;\n"
                                                 "font: 15pt \"Torus Pro\";")


        self.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = UserTab()

    sys.exit(app.exec_())
