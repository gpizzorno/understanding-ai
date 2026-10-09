-- Pre-render script (see _quarto.yml): copy the notebook into the site.
--
-- The notebook lives in code/, where it can be opened in Jupyter or Colab. Quarto can only
-- render files inside the project (docs/), so each build copies it to unit_3/, where the site
-- shows it with its saved outputs. The copy is ignored by git: edit code/ner_pipeline.ipynb.

local source = '../code/ner_pipeline.ipynb'
local target = 'unit_3/ner_pipeline.ipynb'

local input = assert(io.open(source, 'rb'))
local content = input:read('a')
input:close()

local output = assert(io.open(target, 'wb'))
output:write(content)
output:close()
