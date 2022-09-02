import pandas

if __name__ == "__main__":
    courses = pandas.read_excel('export.xlsx', usecols='A:F')
    courses.columns = ['code', 'name', 'requirement_type', 'type', 'semester', 'is_course']
    courses = courses.drop(['type', 'is_course'], axis=1)
    courses['start_year'] = courses['semester'].str.split('/').str[0]
    courses['end_year'] = '20' + courses['semester'].str.split('/').str[1]
    courses['semester_season'] = courses['semester'].str.split('/').str[2]
    courses['semester_season'] = courses['semester_season'].str.replace('1', 'fall')
    courses['semester_season'] = courses['semester_season'].str.replace('2', 'spring')
    courses.to_csv('export.csv', index=False)
