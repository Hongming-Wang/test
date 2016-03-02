
import numpy as np
import pandas as pd

import rpy2.robjects as robj
import rpy2.robjects.pandas2ri
from rpy2.robjects.packages import importr

x = np.random.normal(loc = 5, scale = 2, size = 10)

print x

y = x + np.random.normal(loc=0, scale=2, size=10)

print y

testData = pd.DataFrame({"x":x, "y":y})

print testData

plotFunc = robj.r('''
library(ggplot2)
function(df, ignore){
p <- ggplot(df, aes(x, y)) +
geom_point()
ggsave('rpy2_magic.pdf', plot=p)
}'''
)

#gr = importr('grDevices')

robj.pandas2ri.activate()

testData_R = robj.conversion.py2ri(testData)

plotFunc(testData_R, 'hello')

#raw_input()

#gr.dev_off()


