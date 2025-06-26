# 📊 A/B Testing for Marketing Campaign Conversion Analysis

<p align="center">
  <img src="A_B Test/images/A_B testing_banner.png" alt="A/B Testing Banner" width="100%">
</p>


This project explores whether digital advertisements significantly influence user conversions using real-world A/B testing data. It demonstrates how to evaluate campaign effectiveness through statistical testing, EDA, and proper assumption validation.

---

## 🎯 Objective

The primary goals of this analysis are to:

- Assess if **users exposed to ads** converted at a higher rate than those who saw public service announcements (PSAs).
- Determine whether the **day** and **hour** of ad exposure significantly affect user conversion behavior.
- Use statistical testing to validate whether observed differences are meaningful or due to random chance.

---

## 🧠 Key Insights

- ✅ **Ad exposure leads to significantly higher conversions** than control group (Chi-Square test, p < 0.0001).
- ⏱️ **Time of exposure matters** — both the day and hour when users saw the most ads significantly influenced conversions.
- ❌ Normality and equal variance assumptions were violated (Shapiro-Wilk & Levene’s tests).
- ✅ The **Mann-Whitney U test** confirmed that ad exposure differed significantly between converted and non-converted users.

---

## 📊 Methods Used

- **Chi-Square Test of Independence** – to explore categorical variable associations with conversion.
- **Shapiro-Wilk Test** – to assess normality of ad exposure distribution.
- **Levene’s Test** – to assess equality of variances.
- **Mann-Whitney U Test** – to compare non-normally distributed groups.

---

## 🧰 Tech Stack

- Python
- pandas, seaborn, matplotlib
- scipy.stats, statsmodels

---

## 📁 Project Structure


📁 This project is hosted on GitHub.  
Feel free to explore the code, data, and full analysis:

👉 [View this project on GitHub](https://github.com/Shihamfm/A-B-Testing)

[![GitHub Repo](https://img.shields.io/badge/View_on-GitHub-24292e?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Shihamfm/A-B-Testing)

---
