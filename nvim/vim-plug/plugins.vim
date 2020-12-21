call plug#begin('~/.config/nvim/autoload/plugged')

" Auto completes '(' '[' '{' pairs
Plug 'jiangmiao/auto-pairs'
"surround
Plug 'tpope/vim-surround'
" fuzzy finder
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
" makes sure fzf searches from project base using .git repo
Plug 'airblade/vim-rooter'
" better autocomplete, hopefully it works
Plug 'https://github.com/Valloric/YouCompleteMe.git'
"shitty autocomplete
"Plug 'neoclide/coc.nvim', {'branch': 'release'}
"better syntax support/highlighting
Plug 'sheerun/vim-polyglot'
"highlighting for f,F,t,T ops in vim
Plug 'unblevable/quick-scope'
"autocomplete html tags
Plug 'mattn/emmet-vim'
"not quite sure what below plugin is
"Plug 'mbbill/undotree'
"ranger plugin
"Plug 'kevinhwang91/rnvimr', {'do': 'make sync'}
"status line
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
"themes
Plug 'joshdick/onedark.vim'
Plug 'morhetz/gruvbox'
"automatically sort python imports
Plug 'fisadev/vim-isort'
"async autocomplete
"Plug 'Shougo/deoplete.nvim', {'do': ':autocmd VimEnter * UpdateRemotePlugins'}
"python autocompletion
"Plug 'deoplete-plugins/deoplete-jedi'
"autocomplete from other open files
Plug 'Shougo/context_filetype.vim'
"highlight matching html tags
Plug 'valloric/MatchTagAlways'
"linters
Plug 'neomake/neomake'

call plug#end()
