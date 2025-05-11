def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Count apples landing on the house
    apples_on_house = sum(1 for d in apples if s <= a + d <= t)
    # Count oranges landing on the house
    oranges_on_house = sum(1 for d in oranges if s <= b + d <= t)
    
    print(apples_on_house)
    print(oranges_on_house)