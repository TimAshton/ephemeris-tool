from data_sources.JPLHorizons import JPLHorizons

if __name__ == "__main__":
    ds = JPLHorizons()
    
    parsed_results = ds.get_major_bodies()

    # print(parsed_results)
