mes=$1

if [[ -n "$mes" ]]; then
    scrapy crawl salary_spider -t csv -o ../../data/salary.csv -a month=$mes
else
    scrapy crawl salary_spider -t csv -o ../../data/salary.csv
fi