def towerHanoi(source,destination,extra,numberOfDiscs):
    if numberOfDiscs<=0:
        return
    towerHanoi(source,extra,destination,numberOfDiscs-1)
    print(f'Moving disc {numberOfDiscs} from {source} to {destination}')
    towerHanoi(extra,destination,source,numberOfDiscs-1)

if __name__ == '__main__':
    towerHanoi('i','j','k',4)