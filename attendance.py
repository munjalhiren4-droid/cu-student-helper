# attendance.py - Written by Hiren Munjal (26BCS10584 | munjalhiren4-droid)

def check_attendance(attended, total):
    if total == 0:
        return 0.0, False
    pct = (attended / total) * 100
    eligible = pct >= 75.0  # Chandigarh University 75% Attendance Rule
    return round(pct, 2), eligible
