"
"
"jack's vimrc
"
"""""""""""""colorscheme
set background=dark
"set background=light


colorscheme gruvbox	"sets color scheme to gruvbox
let g:gruvbox_contrast_dark='medium'	" sets contrast to medium: options are: soft, medium, hard
"let g:gruvbox_contrast_light='medium'
"
"
"colorscheme zenburn
"let g:zenburn_high_Contrast = 1
""""""""""""""""""""""""""""""""""

"vim commands:
":ls -> gives list of files that have been opened during session (buffers of
"the files)
"
":b [unique_substr] file from :ls command that has that unique substr in its
"name
"

set noswapfile "vim will not create swap files
set nobackup
set undodir=~/.vim/undodir
set undofile

" enter the current millenium
set nocompatible "stops vim from trying to be vi

"allows vim to act as though it has a fuzzy file finder
"vim will search in subfolders for file as well
"provides tab completion for all file-related tasks
"use command ":find filename.extension" and vim will
"search curr working dir (cwd) and all sub-directories
"for the file and open it up when found
"
"to make fuzzy, use * at beginning or end to find all files with particular
"phrase (basic pattern recognition)
set path+=** 
syntax enable "highlight syntax
set guicursor=n-v-c:block-Cursor "sets cursor to block
                                 "does not work in windows pwrshell
set eol "writes end of line at end of file
set fixeol "make sure last line in file has EOL
set showmode "display mode at bottom of screen
set noesckeys   "stops escape key delay
                "but also removes escape sequence functionality
set smartcase "no ignore if string contains caps
set ruler	"displays cursor position bottom left
set number 	"display line numbers
set relativenumber "display line numbers in relative fashion
set nowrap	"turns off wrapping for long lines
set noerrorbells    "turns off audible bells
set splitbelow  " split files will be opened below
set splitright  " vsp files will be opened to the right of current file:w
set smartindent "turns on smart indenting
set breakindent "wrapped lines follow the indent of their line
set tabstop=4	" number of visual spaces per Tab
set softtabstop=4	" number of spaces in Tab when editing
set expandtab	" Tabs are spaces
set showcmd	" show command in bottom bar
set cursorline	"highlight current line
set cursorcolumn "highlight current column
set wildmenu    " visual autocomplete for command menu
                " when Tab to autocomplete, gui menu of all matches will pop up

set lazyredraw  " stops vim from redrawing screen as much
                " allows for faster macros in the future

set showmatch   "highlights matching [{()}]
set incsearch    " search as characters are entered
"set hlsearch	"highlights seach patter

""""""""""""""""""""FOLDING

"set foldenable     " enables folding
"set foldnestmax=10     " 10 nested fold max
"set foldlevelstart=10  "open most folds by default
                        " foldlevelstart is starting fold level for opening new buffer
                        " if set to 0, all folds will be closed
                        " if set to 99, all folds always open
"nnoremap <space> za    " space opens/closes folds
"set foldmethod=indent  " folds based on indent level

"""""""""""""""""""""MOVEMENT
" move by visual line instead of logical
nnoremap j gj
nnoremap k gk


""""""""""""""""""VERBOSITY
"disables backspace "i cant handle it anymore!
"inoremap <BS> <Nop> 

let mapleader=" "   " <space> replaces \ as mapleader

nnoremap <leader>ev :vsp $MYVIMRC<CR>       " ,ev is shorcut for editing vimrc
nnoremap <leader>sv :source $MYVIMRC<CR>    " ,sv saves recently edited vimrc

" saves all open tabs for next session
" open is back up with vim -S
nnoremap <leader>s :mksession<CR>



""""""""""""""""""""""""""""""""PLUGIN MANAGER
call plug#begin('~/.vim/plugged')
    Plug 'morhetz/gruvbox'
    Plug 'jnurmine/Zenburn'
    Plug 'https://github.com/kien/ctrlp.vim.git'
    Plug 'https://github.com/Valloric/YouCompleteMe.git'
    "Plug 'vim-utils/vim-man'
call plug#end()



"""""""""courtesy of thePrimagen youtube channel
let g:ctrlp_user_command = ['.git/', 'git --git-dir=%s/.git ls-files -oc --exclude-standard']
let g:ctrlp_use_caching = 0  "new file shows up in search w/o restarting vim

""""""""""split window movement"""""""""""""
nnoremap <leader>h :wincmd h<CR>  "<leader>h shifts to right pane
nnoremap <leader>j :wincmd j<CR>  "<leader>j shifts to right pane
nnoremap <leader>k :wincmd k<CR>  "<leader>k shifts to right pane
nnoremap <leader>l :wincmd l<CR>  "<leader>l shifts to right pane
""""""""""""""""""""""""""""""""""""""""""""

nnoremap <leader>gd :YcmCompleter GoTo<CR>
"nnorempa <silent> <leader>gf :YcmCompleter FixIt<CR>
