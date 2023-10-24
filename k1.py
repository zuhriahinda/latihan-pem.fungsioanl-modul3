def konversi(minggu=0):
    def hari(hari=0):
        def jam(jam=0):
            def menit(menit=0):
                return ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit)
            return menit
        return jam
    return hari


data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

outputData = []

for data_item in data:
    parts = data_item.split()
    minggu = int(parts[0])
    hari = int(parts[2])
    jam = int(parts[4])
    menit = int(parts[6])
    konvert = konversi(minggu)(hari)(jam)(menit)
    outputData.append(konvert)

print("OutputData = ", outputData)  # [350001, 58091, 72333]
