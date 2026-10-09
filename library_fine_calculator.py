"""
Library Fine Calculator - Tax Slab Based System
Calculates fine based on days late with detailed breakdown
"""

def calculate_fine(days):
    """Calculate library fine using tax slab system"""
    if days <= 0:
        return 0, []
    
    slabs = [(5, 20), (5, 30), (float('inf'), 40)]
    fine = 0
    details = []
    remaining = days
    slab_start = 1
    
    for slab_days, rate in slabs:
        if remaining <= 0:
            break
        days_in_slab = min(remaining, slab_days)
        slab_fine = days_in_slab * rate
        fine += slab_fine
        details.append(f"Days {slab_start}-{slab_start + days_in_slab - 1}: {days_in_slab} × Rs.{rate} = Rs.{slab_fine}")
        remaining -= days_in_slab
        slab_start += days_in_slab
    
    return fine, details

def main():
    print("\n" + "="*50)
    print("LIBRARY FINE CALCULATOR".center(50))
    print("="*50)
    print("\nFine Rules:")
    print("  Days 1-5:   Rs. 20 per day")
    print("  Days 6-10:  Rs. 30 per day")
    print("  Days >10:   Rs. 40 per day\n")
    
    while True:
        try:
            days = int(input("Enter days late (0 to exit): "))
            if days == 0:
                print("Thank you! Goodbye.\n")
                break
            if days < 0:
                print("❌ Days cannot be negative!\n")
                continue
            
            total_fine, breakdown = calculate_fine(days)
            
            print("\n" + "-"*50)
            print(f"Total Days Late: {days}")
            print("-"*50)
            print("Calculation Breakdown:")
            for detail in breakdown:
                print(f"  {detail}")
            print("-"*50)
            print(f"💰 Total Fine: Rs. {total_fine}")
            print("="*50 + "\n")
            
        except ValueError:
            print("❌ Please enter a valid number!\n")

if __name__ == "__main__":
    main()
