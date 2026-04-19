import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
sns.set_context("paper")

df = pd.read_csv(r"C:\Users\C9IN\Desktop\coding\Python\DataAnalytics_Project\Data\Social_dataset.csv")

df["length_category"] = pd.cut(
    df["post_length"],
    bins=[0,50,100,1000],
    labels=["Short","Medium","Long"]
)

fig = plt.figure(figsize=(13,9))
gs = fig.add_gridspec(3,2)

fig.suptitle("Social Media Dashboard", fontsize=16, fontweight='bold')

ax1 = fig.add_subplot(gs[0,0])
sns.barplot(data=df, x="platform", y="engagement_rate", errorbar=None, ax=ax1)
ax1.set_title("Platform")

ax2 = fig.add_subplot(gs[0,1])
sns.barplot(data=df, x="post_type", y="engagement_rate", errorbar=None, ax=ax2)
ax2.set_title("Post Type")

ax3 = fig.add_subplot(gs[1,0])
sns.barplot(data=df, x="length_category", y="engagement_rate", errorbar=None, ax=ax3)
ax3.set_title("Length")

sample = df.sample(800)

ax4 = fig.add_subplot(gs[1,1])
sns.scatterplot(data=sample, x="likes", y="engagement_rate", s=20, alpha=0.5, ax=ax4)
ax4.set_title("Likes")

ax5 = fig.add_subplot(gs[2,0])
sns.scatterplot(data=sample, x="shares", y="engagement_rate", s=20, alpha=0.5, ax=ax5)
ax5.set_title("Shares")

ax6 = fig.add_subplot(gs[2,1])
corr = df[["views","likes","comments","shares","engagement_rate"]].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cbar=False, ax=ax6)
ax6.set_title("Correlation")

plt.tight_layout(rect=[0,0,1,0.96])
plt.show()