capitals = {
    "Україна": "Київ",
    "Польща": "Варшава",
    "Франція": "Париж"
}
print("Початковий словник:", capitals)
country = "Польща"
print("Столиця країни", country, "-", capitals[country])
capitals["Німеччина"] = "Берлін"
print("Після додавання країни:", capitals)
capitals["Франція"] = "Ліон"
print("Після зміни столиці:", capitals)
del capitals["Польща"]
print("Оновлений словник:", capitals)