# coding: utf-8
YEAR_SCOPE = (
    (0, u'年'),
    (1942, '1942'),
    (1943, '1943'),
    (1944, '1944'),
    (1945, '1945'),
    (1946, '1946'),
    (1947, '1947'),
    (1948, '1948'),
    (1949, '1949'),
    (1950, '1950'),
    (1951, '1951'),
    (1952, '1952'),
    (1953, '1953'),
    (1954, '1954'),
    (1955, '1955'),
    (1956, '1956'),
    (1957, '1957'),
    (1958, '1958'),
    (1959, '1959'),
    (1960, '1960'),
    (1961, '1961'),
    (1962, '1962'),
    (1963, '1963'),
    (1964, '1964'),
    (1965, '1965'),
    (1966, '1966'),
    (1967, '1967'),
    (1968, '1968'),
    (1969, '1969'),
    (1970, '1970'),
    (1971, '1971'),
    (1972, '1972'),
    (1973, '1973'),
    (1974, '1974'),
    (1975, '1975'),
    (1976, '1976'),
    (1977, '1977'),
    (1978, '1978'),
    (1979, '1979'),
    (1980, '1980'),
    (1981, '1981'),
    (1982, '1982'),
    (1983, '1983'),
    (1984, '1984'),
    (1985, '1985'),
    (1986, '1986'),
    (1987, '1987'),
    (1988, '1988'),
    (1989, '1989'),
    (1990, '1990'),
    (1991, '1991'),
    (1992, '1992'),
    (1993, '1993'),
    (1994, '1994'),
    (1995, '1995'),
    (1996, '1996'),
    (1997, '1997'),
    (1998, '1998'),
    (1999, '1999'),
    (2000, '2000'),
    (2001, '2001'),
    (2002, '2002'),
    (2003, '2003'),
    (2004, '2004'),
    (2005, '2005'),
    (2006, '2006'),
    (2007, '2007'),
    (2008, '2008'),
    (2009, '2009'),
    (2010, '2010'),
    (2011, '2011'),
    (2012, '2012'),
    (2013, '2013'),
    (2014, '2014'),
    (2015, '2015'),

)

MONTH_SCOPE = (
    (0, u'月'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
    (11, '11'),
    (12, '12'),
)

COMPANY_NATURE = (
    ('', u'请选择'),
    (1, u'外资(欧美)'),
    (2, u'外资(非欧美)'),
    (3, u'合资(欧美)'),
    (4, u'合资(非欧美)'),
    (5, u'国企'),
    (6, u'民营公司'),
    (7, u'外企代表处'),
    (8, u'政府机关'),
    (9, u'事业单位'),
    (10, u'非盈利机构'),
    (11, u'其他性质')
    )

EDUCATION_TYPE = (
    (u'', u'请选择'),
    (1, u'小学'),
    (2, u'初中'),
    (3, u'中技'),
    (4, u'中专'),
    (5, u'大专'),
    (6, u'本科'),
    (7, u'MBA'),
    (8, u'硕士'),
    (9, u'博士'),
    (10, u'其它')
)

EDUCATION_TYPE_JOB = (
    (0, u'不限'),
    (1, u'小学'),
    (2, u'初中'),
    (10, u'高中'),
    (3, u'中技'),
    (4, u'中专'),
    (5, u'大专'),
    (6, u'本科'),
    (7, u'MBA'),
    (8, u'硕士'),
    (9, u'博士'),
    )

SEARCH_TYPE = (
    (0, u'职位名'),
    (1, u'公司名')
)

SEARCH_PERSON_TYPE = (
    (0, u'职位名'),
    (1, u'姓名')
)

EXPERIENCE_TYPE = (
    (0, u'不限'),
    (1, u'1年以上'),
    (2, u'2年以上'),
    (3, u'3-5年'),
    (4, u'5-10年'),
    (5, u'10年以上')
)

SEX_TYPE = (
    (0, u'不限'),
    (1, u'男'),
    (2, u'女')
)

SALARY_TYPE = (
    (0, u'-面议-'),
    (1, u'1500以下'),
    (2, u'1500-2000'),
    (3, u'2001-3000'),
    (4, u'3001-4000'),
    (5, u'4001-6000'),
    (6, u'6001-10000'),
    (7, u'10000-20000'),
    (8, u'20000以上'),
)

PERSON_ACTION_TYPE = (
    ('store', u'收藏'),
    ('apply', u'申请'),
)

COMPANY_ACTION_TYPE = (
    ('store', u'收藏'),
    ('invite', u'邀请'),
)

JOB_STATE_TYPE = (
    (0, u'目前处于离职状态，可立即上岗'),
    (1, u'目前在职，正考虑换个环境'),
    (2, u'对现有工作很满意，有更好机会才考虑'),
    (3, u'应届生'),
    (4, u'目前暂无跳槽打算')
)

ATTENDANCE_TIME = (
    (1, u'随时到岗'),
    (2, u'三天内'),
    (3, u'两周内'),
    (4, u'一个月内'),
    (5, u'三个月内'),
    (6, u'待定')
)

ATTENDANCE_TIME_SEARCH_JOB = (
    (0, u'不限'),
    (1, u'随时到岗'),
    (2, u'三天内'),
    (3, u'两周内'),
    (4, u'一个月内'),
    (5, u'三个月内'),
    (6, u'待定')
)