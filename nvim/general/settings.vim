"set leader
let g:mapleader = "\<Space>"
"set emmet leader key
"let g:user_emmet_leader_key='<C-Z>'

syntax enable                    "Enables syntax highlighting
set hidden                       "required to keep multiple buffers open
set splitright
set nowrap                       "text does not wrap to next line
set encoding=utf-8               "the encoding is displayed
set pumheight=10                 "makes popup menu smaller
set fileencoding=utf-8           "encoding written to file
set ruler                        "show cursor pos all the time
set cmdheight=2                  "More space for displaying messages
set iskeyword+=-                 "treat dash separated words as a word text object
set t_Co=256                     "support 256 colors
"set conceallevel=0              "so can see '' in markdown files
set tabstop=4                    "insert 4 spaces for tabs
set shiftwidth=4                 "change number of space chars inserted for indent
set smarttab                     "makes tabbing smarter
set expandtab                    "converts tabs to spaces
set autoindent
set smartindent                  "good autoindent
set laststatus=0                 "always display status line
set number relativenumber        "show number lines relative to cursor
set cursorline                   "highlight current line
set nohlsearch                   ""turn off search highlighting
set background=dark              "sets dark background
set showtabline=4                "show tabs at all times
set noshowmode                   "done show current mode, have status bar at all times so do not need showmode
set updatetime=300               "faster completion
set timeoutlen=100               "default timeout is 1000ms
set ttimeoutlen=0                "used for key code delays"
"set formatoptions-=cro           "stop newline continuation of comments
set clipboard+=unnamedplus        "copy-paste between vim and everything else
set fixeol                       "make sure last line in file has EOL
set ignorecase
set colorcolumn=80
set wildmenu                     " visual autocomplete for command menu
                                 " when Tab to autocomplete, gui menu of all matches will pop up
set lazyredraw                   " stops vim from redrawing screen as much
                                 " allows for faster macros in the future
set completeopt+=noinsert        "needed so deoplete can auto select first suggestion"
set completeopt-=preview         "comment line to see autocomplete preview window"
set scrolloff=3                  "keep cursor 3 lines away from screen border when scrolling"


set noswapfile                   "vim will not create swap files
set nobackup
set undodir=~/.config/nvim/undodir
set undofile


"delete empty spaces at end of lines on save for python files
autocmd BufWritePre *.py :%s/\s\+$//e
"run linter on write
autocmd! BufWritePost * Neomake

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"check code as python3 by default
let g:neomake_python_python_maker = neomake#makers#ft#python#python()
let g:neomake_python_flake8_maker = neomake#makers#ft#python#flake8()
let g:neomake_python_python_maker.exe = 'python3 -m py_compile'
let g:neomake_python_flake8_maker.exe = 'python3 -m flake8'

"disabling error messages inside the buffer, next to the problematic line
let g:neomake_virtualtext_current_error = 0


"Deoplete *******
"let g:deoplete#enable_at_startup = 1
"call deoplete#custom#option({
"\  'ignore_case': v:true,
"\  'smart_case': v:true,
"\})

"complete with words from any open file
let g:context_filetype#same_filetypes = {}
let g:context_filetype#same_filetypes._ = '_'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

au! BufWritePost $MYVIMRC source %        "auto source when writing to init.vm alternatively you can run :source $MYVIMRC
