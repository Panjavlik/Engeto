import csv
import seaborn as sns
sns.set_theme(context="notebook", style="darkgrid", palette="deep",
          font="sans-serif", font_scale=1, color_codes=True, rc=None)

dataset = open("Salary_Data.csv", "r")
data = tuple(csv.DictReader(dataset))
dataset.close()
df = {
    "YearsExperience": [float(x["YearsExperience"]) for x in data],
    "Salary": [int(x["Salary"].replace(".00", "")) for x in data],
}

sns.lineplot(
    data=df, x="YearsExperience", y="Salary"
)