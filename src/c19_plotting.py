import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from pandas.plotting import register_matplotlib_converters

plt.rcParams['figure.figsize'] = [12, 5]

class C19Plot(object):
    def __init__(self, daily_data, gov_dataset):
        self.df = daily_data
        self.df_hspc = gov_dataset
        self.x = self.df['date']
        self.x_hspc = self.df_hspc['Date']

    def daily_death_vs_icu(self):
        # ICU Cases vs Deaths
        x = self.df['date']
        fig,ax = plt.subplots()
        plt.title("Daily Deaths Vs ICU Cases")
        plt.plot(self.x, self.df['c19_icu_cases_rm'], label="Daily C19 ICU Cases (3 Day RM)",  marker='o')
        plt.bar(self.x, self.df['new_deaths'], label='Daily Death Updates', color="lightgrey")
        plt.plot(self.x, self.df['new_deaths_rm'], label='Daily Deaths (3 Day RM)', marker='o')
        monthyearFmt = mdates.DateFormatter('%d %b')
        ax.xaxis.set_major_formatter(monthyearFmt)
        ax.set_xticks(self.x)
        plt.xticks(rotation=45)
        plt.legend()
        plt.minorticks_off()
        plt.savefig("output/daily_deaths_vs_icu.png")
        plt.show()

    def daily_icu_availability(self):
        # ICU Availability
        fig,ax = plt.subplots()
        plt.title("Daily ICU Availability")
        plt.bar(self.x, self.df['c19_icu_cases'], label="Current C19 ICU Cases", color="lightgrey")
        plt.plot(self.x, self.df['c19_icu_cases_rm'], label="Current C19 ICU Cases (3 Day RM)",  marker='o')
        plt.plot(self.x, self.df['available_icu_beds_rm'], label='Current Available ICU Beds (3 Day RM)', marker='o')
        monthyearFmt = mdates.DateFormatter('%d %b')
        ax.xaxis.set_major_formatter(monthyearFmt)
        ax.set_xticks(self.x)
        plt.xticks(rotation=45)
        plt.legend()
        plt.minorticks_off()
        plt.savefig("output/daily_icu_avail.png")
        plt.show()

    def daily_icu_vs_ventilation(self):
        # ICU Cases Vs Ventilation Case
        fig,ax = plt.subplots()
        plt.title("Daily Ventilation Cases Vs ICU Cases Vs Available ICU Beds")
        plt.plot(self.x, self.df['c19_icu_cases_rm'], label="Daily C19 ICU Cases (3 Day RM)",  marker='o')
        plt.bar(self.x, self.df['c19_ventilated_cases'], label='Daily Confirmed c19 Ventilation cases', color="lightgrey")
        plt.plot(self.x, self.df['c19_ventilated_cases_rm'], label='c19 Ventilation cases (3 Day RM)', marker='o')
        plt.plot(self.x, self.df['available_icu_beds_rm'], label='Daily Available ICU Beds (3 Day RM)', marker='o')
        monthyearFmt = mdates.DateFormatter('%d %b')
        ax.xaxis.set_major_formatter(monthyearFmt)
        ax.set_xticks(self.x)
        plt.xticks(rotation=45)
        plt.legend(loc='lower left')
        plt.minorticks_off()
        plt.savefig("output/daily_ventilation_vs_icu.png")
        plt.show()

    def hspc_daily_deaths(self):
        # C19 Deaths
        fig,ax1 = plt.subplots()
        plt.title("Daily C19 Deaths")

        ax1.plot(self.x_hspc, self.df_hspc['ConfirmedCovidDeaths_rm'], label='Daily C19 Deaths (3 Day RM)', marker='o', zorder=3)
        ax1.bar(self.x_hspc, self.df_hspc['ConfirmedCovidDeaths'], label='Daily C19 Deaths', color="lightgrey", zorder=1)
        ax1.set_ylabel('Daily C19 Deaths')

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        color = 'tab:red'
        ax2.plot(self.x_hspc, self.df_hspc['TotalCovidDeaths'], label='Total C19 Deaths', marker='o', color=color, zorder=3)
        ax2.set_xticks(self.x_hspc)
        ax2.tick_params(axis='y', labelcolor=color)
        ax2.set_ylabel('Total Deaths', color=color)

        monthyearFmt = mdates.DateFormatter('%d %b')
        ax2.xaxis.set_major_formatter(monthyearFmt)
        ax2.set_xticks(self.x_hspc)
        #ax2.legend(loc=0)
        plt.draw()
        ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90, ha='right')

        # ask matplotlib for the plotted objects and their labels
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='upper left')

        fig.tight_layout()
        plt.savefig("output/c19_daily_deaths.png")
        plt.show()

    def hspc_icu(self):
        # C19 ICU
        fig,ax1 = plt.subplots()
        plt.title("Daily C19 ICU")

        #ax1.plot(x, df_hspc['ConfirmedCovidDeaths_rm'], label='Daily C19 Deaths (3 Day RM)', marker='o', zorder=3)
        ax1.plot(self.x_hspc, self.df_hspc['RequiringICUCovidCases_new_rm'], label='Daily New C19 ICU (3 Day RM)', marker='o', zorder=2)
        ax1.bar(self.x_hspc, self.df_hspc['RequiringICUCovidCases_new'], label='Daily New C19 ICU', color="lightgrey", zorder=1)
        ax1.set_ylabel('Daily ICU')

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        color = 'tab:red'
        ax2.plot(self.x_hspc, self.df_hspc['RequiringICUCovidCases'], label='Total C19 ICU', marker='o', color=color, zorder=3)
        ax2.set_xticks(self.x_hspc)
        ax2.tick_params(axis='y', labelcolor=color)
        ax2.set_ylabel('Total ICU', color=color)

        monthyearFmt = mdates.DateFormatter('%d %b')
        ax2.xaxis.set_major_formatter(monthyearFmt)
        ax2.set_xticks(self.x_hspc)
        plt.draw()
        ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90, ha='right')

        # ask matplotlib for the plotted objects and their labels
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='upper center')

        fig.tight_layout()
        plt.savefig("output/icu_daily.png")
        plt.show()

    def hspc_hospitilisation(self):
        # Total C19 Hospitilisation
        fig,ax1 = plt.subplots()
        plt.title("Daily C19 Hospitilisation All Ages")

        ax1.plot(self.x_hspc, self.df_hspc['HospitalisedCovidCases_new_rm'], label='Daily C19 Hospitalised (3 Day RM)', marker='o', zorder=2)
        ax1.bar(self.x_hspc, self.df_hspc['HospitalisedCovidCases_new'], label='Daily C19 Hospitalised', color="lightgrey", zorder=1)
        ax1.set_ylabel('Daily New Hospitalised')

        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        color = 'tab:red'
        ax2.plot(self.x_hspc, self.df_hspc['HospitalisedCovidCases'], label='Total C19 Hospitalised', marker='o', color=color, zorder=3)
        ax2.set_xticks(self.x_hspc)
        ax2.tick_params(axis='y', labelcolor=color)
        ax2.set_ylabel('Total Hospitalised', color=color)

        monthyearFmt = mdates.DateFormatter('%d %b')
        ax2.xaxis.set_major_formatter(monthyearFmt)
        ax2.set_xticks(self.x_hspc)
        plt.draw()
        ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90, ha='right')

        # ask matplotlib for the plotted objects and their labels
        lines, labels = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax2.legend(lines + lines2, labels + labels2, loc='upper center')

        fig.tight_layout()
        plt.savefig("output/hospatilsation_daily_all_ages.png")
        plt.show()


    def hspc_hospitilisation_less_14(self):
        # Daily C19 Hospitilisation by age < 45
        fig,ax = plt.subplots()
        plt.title("Daily C19 Hospitilisation by age < 14")
        #plt.plot(self.x_hspc, self.df_hspc['HospitalisedAged5_new_rm'], label='Daily C19 Hospitalised <5 (3 Day RM)', marker='o')
        #plt.plot(self.x_hspc, self.df_hspc['HospitalisedAged5to14_new_rm'], label='Daily C19 Hospitalised 5-14(3 Day RM)', marker='o')

        plt.plot(self.x_hspc, self.df_hspc['HospitalisedAged5_new'], label='Daily C19 Hospitalised <5', marker='o')
        plt.plot(self.x_hspc, self.df_hspc['HospitalisedAged5to14_new'], label='Daily C19 Hospitalised 5-14', marker='o')

        monthyearFmt = mdates.DateFormatter('%d %b')
        ax.xaxis.set_major_formatter(monthyearFmt)
        ax.set_xticks(self.x_hspc)
        plt.xticks(rotation=45)
        plt.legend()
        plt.minorticks_off()
        plt.tight_layout()
        plt.savefig("output/hospatilsation_daily_by_age_less_than_14.png")
        plt.show()

    def hspc_hospitilisation_less_45(self):
        # Daily C19 Hospitilisation by age < 45
        fig,ax = plt.subplots()
        plt.title("Daily C19 Hospitilisation by age < 45")
        plt.plot(self.x_hspc, self.df_hspc['HospitalisedAged5_new_rm'], label='Daily C19 Hospitalised <5 (3 Day RM)', marker='o')
        plt.plot(self.x_hspc, self.df_hspc['HospitalisedAged5to14_new_rm'], label='Daily C19 Hospitalised 5-14(3 Day RM)', marker='o')
        plt.plot(self.x_hspc, self.df_hspc["HospitalisedAged25to34_new_rm"], label='Daily C19 Hospitalised 25-34 (3 Day RM)', marker='o')
        plt.plot(self.x_hspc, self.df_hspc["HospitalisedAged35to44_new_rm"], label='Daily C19 Hospitalised 35-44 (3 Day RM)', marker='o')

        monthyearFmt = mdates.DateFormatter('%d %b')
        ax.xaxis.set_major_formatter(monthyearFmt)
        ax.set_xticks(self.x_hspc)
        plt.xticks(rotation=45)
        plt.legend()
        plt.minorticks_off()
        plt.tight_layout()
        plt.savefig("output/hospatilsation_daily_by_age_less_than_45.png")
        plt.show()

    def hspc_hospitilisation_45_to_65(self):
        fig,ax = plt.subplots()
        plt.title("Daily C19 Hospitilisation by age 45 - 65")
        plt.plot(self.x_hspc, self.df_hspc["HospitalisedAged45to54_new_rm"], label='Daily C19 Hospitalised 45-54 (3 Day RM)', marker='o')
        plt.plot(self.x_hspc, self.df_hspc["HospitalisedAged55to64_new_rm"], label='Daily C19 Hospitalised 55-64 (3 Day RM)', marker='o')

        monthyearFmt = mdates.DateFormatter('%d %b')
        ax.xaxis.set_major_formatter(monthyearFmt)
        ax.set_xticks(self.x_hspc)
        plt.xticks(rotation=45)
        plt.legend()
        plt.minorticks_off()
        plt.tight_layout()
        plt.savefig("output/hospatilsation_daily_by_age_greater_than_45.png")
        plt.show()

    def hspc_hospitilisation_greater_65(self):
        # Daily C19 Hospitilisation by age > 65
        fig,ax = plt.subplots()
        plt.title("Daily C19 Hospitilisation by age > 65")
        plt.plot(self.x_hspc, self.df_hspc["HospitalisedAged65up_new_rm"], label='Daily C19 Hospitalised >65 (3 Day RM)', marker='o')

        monthyearFmt = mdates.DateFormatter('%d %b')
        ax.xaxis.set_major_formatter(monthyearFmt)
        ax.set_xticks(self.x_hspc)
        plt.xticks(rotation=45)
        plt.legend()
        plt.minorticks_off()
        plt.tight_layout()
        plt.savefig("output/hospatilsation_daily_by_age_greater_than_65.png")
        plt.show()