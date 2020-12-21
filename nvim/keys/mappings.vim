"here is where remappings are stored



" Tab in general mode will move to text buffer (switch between recently opened
" files)
map tt :tabnew
nnoremap <TAB> :bnext<CR>
" Shift-TAB will move backwards through buffer
nnoremap <S-TAB> :bprevious<CR>

"move by visual line instead of logical line
nnoremap j gj
nnoremap k gk
"move by words separated by space
"nnoremap w W
"nnoremap b B

"shortcut for quitting w/o saving
nnoremap <leader>q :q!<CR>

"shortcut for editing vimrc
nnoremap <leader>ev :sp $MYVIMRC<CR>       

""""""""""split window movement"""""""""""""
nnoremap <leader>h :wincmd h<CR>  
nnoremap <leader>j :wincmd j<CR> 
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR> 
""""""""""""""""""""""""""""""""""""""""""""

"""""""""""YCM remaps"""""""""""""
nnoremap  <leader>gd :YcmCompleter GoTo<CR>
nnoremap  <leader>gr :YcmCompleter GoToReference<CR>
"nnoremap <leader>rr :YcmCompleter RefactorRename<space>
""""""""""""""""""""""""""""""""""""""""""""

"""""""""""emmet remap"""""""""""
imap <C-Z> <C-Y>,


""""""""""copy/paste mappings""""""""""
nnoremap <leader>p "+p
nnoremap <leader>y "+y
