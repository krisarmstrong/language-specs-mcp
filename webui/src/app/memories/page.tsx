'use client'

import { useState, useEffect } from 'react'
import { Brain, Plus, Trash2, Edit2, Save, X } from 'lucide-react'

interface Memory {
  id: string
  name: string
  content: string
  createdAt: string
  updatedAt: string
}

export default function MemoriesPage() {
  const [memories, setMemories] = useState<Memory[]>([])
  const [selectedMemory, setSelectedMemory] = useState<Memory | null>(null)
  const [isEditing, setIsEditing] = useState(false)
  const [editContent, setEditContent] = useState('')
  const [newMemoryName, setNewMemoryName] = useState('')
  const [showNewForm, setShowNewForm] = useState(false)

  useEffect(() => {
    fetchMemories()
  }, [])

  const fetchMemories = async () => {
    try {
      const res = await fetch('/api/memories')
      const data = await res.json()
      setMemories(data.memories || [])
    } catch (err) {
      console.error('Failed to fetch memories:', err)
    }
  }

  const createMemory = async () => {
    if (!newMemoryName.trim()) return
    try {
      const res = await fetch('/api/memories', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: newMemoryName, content: '' })
      })
      if (res.ok) {
        setNewMemoryName('')
        setShowNewForm(false)
        fetchMemories()
      }
    } catch (err) {
      console.error('Failed to create memory:', err)
    }
  }

  const saveMemory = async () => {
    if (!selectedMemory) return
    try {
      const res = await fetch('/api/memories/' + selectedMemory.id, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ content: editContent })
      })
      if (res.ok) {
        setIsEditing(false)
        fetchMemories()
        setSelectedMemory({ ...selectedMemory, content: editContent })
      }
    } catch (err) {
      console.error('Failed to save memory:', err)
    }
  }

  const deleteMemory = async (id: string) => {
    if (!confirm('Are you sure you want to delete this memory?')) return
    try {
      const res = await fetch('/api/memories/' + id, { method: 'DELETE' })
      if (res.ok) {
        if (selectedMemory?.id === id) setSelectedMemory(null)
        fetchMemories()
      }
    } catch (err) {
      console.error('Failed to delete memory:', err)
    }
  }

  const startEditing = () => {
    if (!selectedMemory) return
    setEditContent(selectedMemory.content)
    setIsEditing(true)
  }

  return (
    <div className="min-h-screen p-8">
      <div className="max-w-6xl mx-auto">
        <header className="mb-8 flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-slate-900 dark:text-white mb-2">
              Memories
            </h1>
            <p className="text-slate-600 dark:text-slate-300">
              Store project-specific notes and context for future sessions
            </p>
          </div>
          <button
            onClick={() => setShowNewForm(true)}
            className="flex items-center gap-2 px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded-lg font-medium transition-colors"
          >
            <Plus className="w-5 h-5" />
            New Memory
          </button>
        </header>

        {showNewForm && (
          <div className="mb-6 bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 p-4">
            <div className="flex gap-4">
              <input
                type="text"
                value={newMemoryName}
                onChange={(e) => setNewMemoryName(e.target.value)}
                placeholder="Memory name (e.g., project-architecture)"
                className="flex-1 px-4 py-2 rounded-lg border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white"
              />
              <button
                onClick={createMemory}
                className="px-4 py-2 bg-green-500 hover:bg-green-600 text-white rounded-lg"
              >
                Create
              </button>
              <button
                onClick={() => setShowNewForm(false)}
                className="px-4 py-2 bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300 rounded-lg"
              >
                Cancel
              </button>
            </div>
          </div>
        )}

        <div className="flex gap-6">
          <div className="w-64 shrink-0">
            <h2 className="text-sm font-semibold text-slate-500 dark:text-slate-400 uppercase mb-3">
              Saved Memories
            </h2>
            {memories.length > 0 ? (
              <div className="space-y-2">
                {memories.map((memory) => (
                  <div
                    key={memory.id}
                    className={[
                      'p-3 rounded-lg cursor-pointer transition-colors group',
                      selectedMemory?.id === memory.id
                        ? 'bg-blue-50 dark:bg-blue-900/30 border border-blue-200 dark:border-blue-800'
                        : 'bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-750'
                    ].join(' ')}
                    onClick={() => {
                      setSelectedMemory(memory)
                      setIsEditing(false)
                    }}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <Brain className="w-4 h-4 text-purple-500" />
                        <span className="text-sm font-medium text-slate-900 dark:text-white truncate">
                          {memory.name}
                        </span>
                      </div>
                      <button
                        onClick={(e) => {
                          e.stopPropagation()
                          deleteMemory(memory.id)
                        }}
                        className="opacity-0 group-hover:opacity-100 p-1 text-red-500 hover:bg-red-50 dark:hover:bg-red-900/30 rounded transition-opacity"
                      >
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </div>
                    <p className="text-xs text-slate-500 dark:text-slate-400 mt-1">
                      {new Date(memory.updatedAt).toLocaleDateString()}
                    </p>
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-sm text-slate-500 dark:text-slate-400">
                No memories saved yet
              </p>
            )}
          </div>

          <div className="flex-1">
            {selectedMemory ? (
              <div className="bg-white dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700">
                <div className="flex items-center justify-between p-4 border-b border-slate-200 dark:border-slate-700">
                  <h3 className="font-medium text-slate-900 dark:text-white">
                    {selectedMemory.name}
                  </h3>
                  <div className="flex gap-2">
                    {isEditing ? (
                      <>
                        <button
                          onClick={saveMemory}
                          className="flex items-center gap-1 px-3 py-1 bg-green-500 hover:bg-green-600 text-white rounded-lg text-sm"
                        >
                          <Save className="w-4 h-4" />
                          Save
                        </button>
                        <button
                          onClick={() => setIsEditing(false)}
                          className="flex items-center gap-1 px-3 py-1 bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300 rounded-lg text-sm"
                        >
                          <X className="w-4 h-4" />
                          Cancel
                        </button>
                      </>
                    ) : (
                      <button
                        onClick={startEditing}
                        className="flex items-center gap-1 px-3 py-1 bg-blue-500 hover:bg-blue-600 text-white rounded-lg text-sm"
                      >
                        <Edit2 className="w-4 h-4" />
                        Edit
                      </button>
                    )}
                  </div>
                </div>
                <div className="p-4">
                  {isEditing ? (
                    <textarea
                      value={editContent}
                      onChange={(e) => setEditContent(e.target.value)}
                      className="w-full h-96 p-4 rounded-lg border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 text-slate-900 dark:text-white font-mono text-sm resize-none"
                      placeholder="Write your notes here..."
                    />
                  ) : (
                    <div className="prose dark:prose-invert max-w-none">
                      <pre className="whitespace-pre-wrap text-sm bg-slate-50 dark:bg-slate-900 p-4 rounded-lg">
                        {selectedMemory.content || 'No content yet. Click Edit to add notes.'}
                      </pre>
                    </div>
                  )}
                </div>
              </div>
            ) : (
              <div className="bg-slate-100 dark:bg-slate-800/50 rounded-xl border-2 border-dashed border-slate-300 dark:border-slate-600 p-12 text-center">
                <Brain className="w-12 h-12 mx-auto text-slate-400 mb-4" />
                <p className="text-slate-500 dark:text-slate-400">
                  Select a memory or create a new one to get started
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}
