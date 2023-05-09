from typing import List, Tuple


def solution(today:str, terms:List[str], privacies:List[str]) -> List[int]:
    #def convert_to_date(days:int) -> Tuple[int, int, int]:
    #    days, day = days // 28, days % 28
    #    year, month = days // 12, days % 12 
    #    return (year, month, day)
    #

    # 1년 1월 1일부터 지난 일수
    def convert_to_days(date:str) -> int:
        year, month, day = map(int, date.split("."))
        return year * 28 * 12 + month  * 28 + day 
    today = convert_to_days(today)
    
    #term별 최소 날짜
    min_date = dict()
    for term in terms:
        term, period = term.split()
        min_date[term] = today - int(period) * 28 + 1
    
    
    answer = []
    for index, privacy in enumerate(privacies, 1):
        date, term = privacy.split()
        if min_date[term] > convert_to_days(date):
            answer.append(index)
        
    return answer
